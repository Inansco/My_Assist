from fastapi import FastAPI
from pydantic import BaseModel

from ai.test_provider import TestProvider


app = FastAPI(
    title="Inansco AI Assistant",
    description="Inansco cross-platform AI assistant API",
    version="1.0.0",
)


ai = TestProvider()


class ChatRequest(BaseModel):
    message: str


@app.get("/api/health")
def health():
    return {
        "status": "online",
        "assistant": "Inansco",
        "version": "1.0.0"
    }


@app.post("/api/chat")
def chat(request: ChatRequest):

    reply = ai.chat(request.message)

    return {
        "message": request.message,
        "reply": reply
    }