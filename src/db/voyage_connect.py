import os
from dotenv import load_dotenv
import voyageai

load_dotenv()

voyage_client=voyageai.Client(api_key=os.environ['VOYAGE_API_KEY'])

try:
    voyage_client = voyageai.Client(api_key=os.environ['VOYAGE_API_KEY'])
    print("Connected to Voyage API")
except Exception as e:
    print("Failed to connect to Voyage API")


