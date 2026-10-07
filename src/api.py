from fastapi import FastAPI, Request
from pydantic import BaseModel
from src.qa import ask

from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()


class AskRequest(BaseModel):
    question: str


@app.post("/ask")
@limiter.limit("10/minute")
def ask_endpoint(request: Request, req: AskRequest):
    return ask(req.question)


@app.get("/health")
def health():
    return {"status": "ok"}

app.state.limiter = limiter

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)