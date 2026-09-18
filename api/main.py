from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from core.brain import Brain


app = FastAPI(
    title="Inansco AI Assistant",
    description="Inansco cross-platform AI assistant API",
    version="1.0.0",
)


brain = Brain()

templates = Jinja2Templates(directory="templates")


class ChatRequest(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.get("/api/health")
def health():
    return {
        "status": "online",
        "assistant": "Inansco",
        "version": "1.0.0"
    }


@app.post("/api/chat")
def chat(request: ChatRequest):

    reply = brain.think(request.message)

    return {
        "message": request.message,
        "reply": reply
    }