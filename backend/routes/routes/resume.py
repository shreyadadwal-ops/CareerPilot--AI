from fastapi import APIRouter, UploadFile, File
import shutil
import os

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

    return {
        "message": "Resume uploaded successfully",
        "filename": file.filename,
        "resume_text": resume_text
    }