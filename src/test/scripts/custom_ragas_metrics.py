import time

from src.llm import get_llm
from src.qa import ask
from src.guardrails import _text# reuse your existing _text() helper

RELEVANCY_PROMPT = (
    "Does the ANSWER directly address the QUESTION asked? "
    "Score from 0.0 (completely off-topic) to 1.0 (fully addresses it). "
    "Reply with only a number.\n\nQUESTION: {question}\n\nANSWER: {answer}"
)

FAITHFULNESS_PROMPT = (
    "What fraction of factual claims in the ANSWER are directly supported by the CONTEXT? "
    "Score from 0.0 (none supported) to 1.0 (all supported). "
    "Reply with only a number.\n\nCONTEXT:\n{context}\n\nANSWER: {answer}"
)

QUERIES = [
    "What caused past database outages related to capacity issues?",
    "What role did DNS play in past outages?",
    "How have certificate expirations caused production incidents?",
    "What kinds of human errors have caused major outages?",
    "What incidents involved Kubernetes or container orchestration?",
]

def score(prompt_template, **kwargs) -> float:
    llm = get_llm()
    resp = llm.invoke(prompt_template.format(**kwargs))
    try:
        return float(_text(resp).strip())
    except ValueError:
        return 0.0  # couldn't parse a score, treat as failure

if __name__ == "__main__":
    relevancy_scores, faithfulness_scores = [], []
    for q in QUERIES:
        result = ask(q)
        if not result["contexts"]:
            continue
        context = "\n---\n".join(result["contexts"])

        rel = score(RELEVANCY_PROMPT, question=q, answer=result["answer"])
        faith = score(FAITHFULNESS_PROMPT, context=context, answer=result["answer"])

        relevancy_scores.append(rel)
        faithfulness_scores.append(faith)
        print(f"{q[:50]:50s} | relevancy={rel:.2f} | faithfulness={faith:.2f}")
        time.sleep(15)

    print(f"\nAvg relevancy: {sum(relevancy_scores)/len(relevancy_scores):.2f}")
    print(f"Avg faithfulness: {sum(faithfulness_scores)/len(faithfulness_scores):.2f}")