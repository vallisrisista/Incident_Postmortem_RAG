import src.db.embeddings as em
from src.db.db_connect import mongo_db as db
from scripts.ingest import incident_collection
import src.db.voyage_connect
INDEX_NAME = "incidents_vector_index"

def search(query: str, k: int = 5, category: str | None = None):
    vec = em.embed([query], input_type="query")[0]

    stage = {
        "index": INDEX_NAME,
        "path": "embedding",
        "queryVector": vec,
        "numCandidates": 100,
        "limit": k,
    }
    if category:
        stage["filter"] = {"category": {"$eq": category}}

    pipeline = [
        {"$vectorSearch": stage},
        {"$project": {"company": 1, "category": 1, "description": 1, "url": 1,
                       "score": {"$meta": "vectorSearchScore"}}},
    ]
    return list(incident_collection.aggregate(pipeline))


if __name__ == "__main__":
    results = search("MongoDB overloaded under load")
    for r in results:
        print(round(r["score"], 3), "-", r["company"], f"[{r['category']}]")
        print("  ", r["description"][:120])
    print("results:", len(results))