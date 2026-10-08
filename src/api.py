from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
from src.qa import ask

from slowapi import Limiter
from slowapi.util import get_remote_address


limiter = Limiter(key_func=get_remote_address)

app = FastAPI()
app.state.limiter = limiter

templates = Jinja2Templates(directory="templates")


class AskRequest(BaseModel):
    question: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/ask")
@limiter.limit("10/minute")
def ask_endpoint(request: Request, req: AskRequest):
    return ask(req.question)


@app.get("/health")
def health():
    return {"status": "ok"}