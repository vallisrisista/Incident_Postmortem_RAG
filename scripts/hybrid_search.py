from urllib3.util import url

from src.db.db_connect import incident_collection as col
from src.db.embeddings import embed

VECTOR_INDEX = "incidents_vector_index"
TEXT_INDEX = "incidents_text_index"


def hybrid_search(query, k=5):
    vec = embed([query], input_type="query")[0]

    pipeline = [
        {"$rankFusion": {
            "input": {
                "pipelines": {
                    "vectorPipeline": [
                        {"$vectorSearch": {
                            "index": VECTOR_INDEX, "path": "embedding",
                            "queryVector": vec, "numCandidates": 100, "limit": 10,
                        }}
                    ],
                    "textPipeline": [
                        {"$search": {
                            "index": TEXT_INDEX,
                            "text": {"query": query, "path": "description"},
                        }},
                        {"$limit": 10},
                    ],
                }
            }
        }},
        {"$limit": k},
        {"$project": {"company": 1, "category": 1, "description": 1, "url":1,
                      "score": {"$meta": "score"}}},
    ]
    return list(col.aggregate(pipeline))
if __name__ == "__main__":
    for r in hybrid_search("certificate expired causing mass outage"):
        print(r.get("score"), "-", r["company"], f"[{r['category']}]", r['description'])