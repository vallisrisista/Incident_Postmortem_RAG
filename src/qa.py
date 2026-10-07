from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langsmith import traceable

from src.llm import get_llm
from scripts.hybrid_search import hybrid_search   # adjust to your actual function/module name
from src.guardrails import validate_query, is_in_scope

ANSWER_PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "Answer the question using ONLY the provided incident summaries. "
     "Cite each claim with (Company, URL). "
     "If the summaries don't contain enough information to answer, say so plainly — "
     "do not guess or use outside knowledge."),
    ("human", "QUESTION: {question}\n\nINCIDENTS:\n{context}"),
])

JUDGE_PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "Check whether every factual claim in the ANSWER is supported by the INCIDENTS. "
     "Reply exactly 'FAITHFUL: yes' or 'FAITHFUL: no - <reason>'."),
    ("human", "INCIDENTS:\n{context}\n\nANSWER:\n{answer}"),
])

@traceable
def _format_context(hits: list[dict]) -> str:
    return "\n---\n".join(
        f"Company: {h['company']}\nCategory: {h['category']}\n"
        f"URL: {h.get('url', 'n/a')}\nSummary: {h['description']}"
        for h in hits
    )

@traceable
def ask(question: str, k: int = 5) -> dict:
    question = validate_query(question)
    if not is_in_scope(question):
        return {"answer": "This question doesn't appear to be about a software incident "
                          "or postmortem — I can only answer within that scope.",
                "sources": [], "faithful": None, "contexts": []}

    hits = hybrid_search(question, k=k)
    if not hits:
        return {"answer": "I couldn't find any incidents relevant to this question.",
                "sources": [], "faithful": None, "contexts": []}

    context = _format_context(hits)
    llm = get_llm()

    answer = (ANSWER_PROMPT | llm | StrOutputParser()).invoke(
        {"question": question, "context": context}
    ).strip()

    verdict = (JUDGE_PROMPT | llm | StrOutputParser()).invoke(
        {"context": context, "answer": answer}
    ).strip()
    faithful = verdict.lower().startswith("faithful: yes")

    if not faithful:
        answer = ("I found related incidents, but couldn't produce an answer that's fully "
                  "grounded in them. Please review the sources directly.")

    return {
        "answer": answer,
        "sources": [{"company": h["company"], "url": h.get("url")} for h in hits],
        "faithful": faithful,
        "judge_notes": None if faithful else verdict,
        "contexts": [h["description"] for h in hits],   # kept for RAGAS, next step
    }