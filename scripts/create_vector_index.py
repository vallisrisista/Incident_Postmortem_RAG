import time


from ingest import incident_collection

from pymongo.operations import SearchIndexModel

INDEX_NAME="incidents_vector_index"
existing=[i["name"] for i in incident_collection.list_search_indexes()]

if INDEX_NAME not in existing:
    print("creating index")
    model = SearchIndexModel(
        name=INDEX_NAME,
        type="vectorSearch",
        definition={
            "fields": [
                {"type": "vector", "path": "embedding",
                 "numDimensions": 1024, "similarity": "cosine"},
                {"type": "filter", "path": "category"},
                {"type": "filter", "path": "company"},
            ]
        },
    )
    incident_collection.create_search_index(model=model)
    print("Index creation requested, waiting until queryable...")
    while not any(i["name"] == INDEX_NAME and i.get("queryable")
                  for i in incident_collection.list_search_indexes()):
        time.sleep(5)
    print("Index ready")