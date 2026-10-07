from pymongo import UpdateOne

import src.db.embeddings as embd
from ingest import incident_collection
#from src.db import embeddings

docs = list(incident_collection.find({"embedding": {"$exists": False}}))

if docs:
    print(f"Found {len(docs)} documents to embed")

    vectors=embd.embed([doc["description"] for doc in docs])
    print(f"embedded {len(vectors)}")

    operation=[
        UpdateOne({"_id": doc["_id"]}, {"$set": {"embedding": vectors}})
        for doc,vectors in zip(docs,vectors)
    ]
    incident_collection.bulk_write(operation)
