import json
from pathlib import Path
from src.db.db_connect import incident_collection

DATA_FILE = Path(__file__).resolve().parent.parent / "src" / "db" / "postmortems.json"

def main():
    with open(DATA_FILE) as f:
        data = json.load(f)
    for r in data:
        r["_id"] = r.pop("id")
    result = incident_collection.insert_many(data)
    print(f"Inserted {len(result.inserted_ids)} documents")

if __name__ == "__main__":
    main()