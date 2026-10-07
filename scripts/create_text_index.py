import time
from ingest import incident_collection
from pymongo.operations import SearchIndexModel
INDEX_NAME="incidents_text_index"
existing =[i["name"] for i in incident_collection.list_search_indexes()]
if INDEX_NAME not in existing:
    print("creating text index")
    model=SearchIndexModel(name=INDEX_NAME,
                           definition={
                               "mappings":{
                                   "dynamic":False,"fields":{
                                       "description":{"type":"string"},
                                   }

                               }
                           }
                           )
    incident_collection.create_search_index(model=model)
    print("Text index creation requested — check Atlas UI in ~1-2 min for Active status")

