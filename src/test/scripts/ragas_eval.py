from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from ragas.llms import LangchainLLMWrapper
from datasets import Dataset
from src.llm import get_llm
from src.qa import ask
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_voyageai import VoyageAIEmbeddings
import os

ragas_embeddings = LangchainEmbeddingsWrapper(
    VoyageAIEmbeddings(model="voyage-4-lite", voyage_api_key=os.environ["VOYAGE_API_KEY"])
)

QUERIES = [
    "What caused past database outages related to capacity issues?",
    "What role did DNS play in past outages?",
    "How have certificate expirations caused production incidents?",
    "What kinds of human errors have caused major outages?",
    "What incidents involved Kubernetes or container orchestration?",
]

rows = []
for q in QUERIES:
    result = ask(q)
    if not result["contexts"]:
        continue  # skip rejected/empty-result queries, RAGAS needs real context
    rows.append({
        "question": q,
        "answer": result["answer"],
        "contexts": result["contexts"],
    })

dataset = Dataset.from_list(rows)

ragas_llm = LangchainLLMWrapper(get_llm())  # reuse your Gemini client, no separate OpenAI key needed

scores = evaluate(
    dataset,
    metrics=[faithfulness, answer_relevancy],
    llm=ragas_llm,
)
print(scores.to_pandas())