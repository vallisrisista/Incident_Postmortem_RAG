import os
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi

load_dotenv()
mongo_client=MongoClient(os.environ['MONGODB_URI'], tlsCAFile=certifi.where())
try:
    mongo_client.admin.command("ping")
    print("connection to mongo db successful")
except Exception as e:
    print("connection to mongo db failed",e)


