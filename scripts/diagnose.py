from src.db.db_connect import incident_collection

print("docs:", incident_collection.count_documents({}))
print("with embedding:", incident_collection.count_documents({"embedding": {"$exists": True}}))

d = incident_collection.find_one({"embedding": {"$exists": True}})
print("embedding length:", len(d["embedding"]) if d else None)

for i in incident_collection.list_search_indexes():
    print("index:", i["name"], "| type:", i.get("type"),
          "| status:", i.get("status"), "| queryable:", i.get("queryable"))
    print("  definition:", i.get("latestDefinition"))