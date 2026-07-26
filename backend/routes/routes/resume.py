from fastapi import APIRouter, UploadFile, File
import shutil
import os

from backend.services.gemini_service import (
    analyze_resume,
    skill_gap_analysis,
    generate_learning_roadmap,
)
from backend.services.resume_service import extract_text_from_pdf

router = APIRouter(tags=["Resume"])

UPLOAD_FOLDER = "backend/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text_from_pdf(file_path)

    analysis = analyze_resume(resume_text)
    skill_gap = skill_gap_analysis(resume_text)
    roadmap = generate_learning_roadmap(resume_text)

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "resume_analysis": analysis,
        "skill_gap_analysis": skill_gap,
        "learning_roadmap": roadmap,
    }