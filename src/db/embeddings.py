import src.db.voyage_connect as vc

def embed(texts:list[str], input_type:str="document") -> list[list[float]]:
    result=vc.voyage_client.embed(texts,input_type=input_type,model="voyage-4-lite")
    return result.embeddings

