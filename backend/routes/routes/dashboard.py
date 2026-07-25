from fastapi import APIRouter

router = APIRouter(tags=["Dashboard"])


@router.get("/dashboard")
def get_dashboard():
    return {
        "student": {
            "name": "Demo Student",
            "email": "demo@example.com",
            "degree": "B.Tech"
        },
        "career_recommendation": "AI Engineer",
        "resume_score": 90,
        "skill_gap": [
            "Docker",
            "FastAPI",
            "AWS"
        ],
        "learning_roadmap": [
            "Week 1: Python",
            "Week 2: SQL",
            "Week 3: FastAPI",
            "Week 4: AI Project"
        ]
    }