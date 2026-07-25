from fastapi import FastAPI
from backend.routes.routes.profile import router as profile_router
from backend.database import Base,engine
from backend.models.models.student import Student
from backend.models.models.user import User
from backend.routes.routes.auth import router as auth_router
from backend.routes.routes.resume import router as resume_router
from backend.routes.routes.chatbot import router as chatbot_router
from backend.routes.routes.dashboard import router as dashboard_router

app = FastAPI(
    title="CareerPilot AI",
    version="1.0"
)
Base.metadata.create_all(bind=engine)

app.include_router(profile_router)
app.include_router(auth_router)
app.include_router(resume_router)
app.include_router(chatbot_router)
app.include_router(dashboard_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to CareerPilot AI 🚀"
    }