from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.gemini_service import chatbot_response

router = APIRouter(tags=["AI Chatbot"])


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):
    answer = chatbot_response(request.question)

    return {
        "question": request.question,
        "answer": answer
    }