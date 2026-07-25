import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")


# Career Recommendation
def generate_career_recommendation(student):
    prompt = f"""
You are an expert career counselor.

Student Details:

Name: {student.name}
Degree: {student.degree}
Skills: {student.skills}
Interests: {student.interests}
Career Goal: {student.career_goal}

Suggest:
1. Best Career
2. Why it suits the student
3. Skills to improve
4. Certifications
5. Learning roadmap
"""

    response = model.generate_content(prompt)
    return response.text


# Resume Analysis
def analyze_resume(resume_text: str):
    prompt = f"""
You are an expert career counselor.

Analyze the following resume.

Resume:
{resume_text}

Return:

Resume Score
Strengths
Weaknesses
Missing Skills
Recommended Careers
Recommended Courses
"""

    response = model.generate_content(prompt)
    return response.text


# Skill Gap Analysis
def skill_gap_analysis(resume_text: str):
    prompt = f"""
Analyze this resume and provide:

1. Current Skills
2. Missing Skills
3. Recommended Skills
4. Best Online Courses
5. Estimated Learning Time

Resume:
{resume_text}
"""

    response = model.generate_content(prompt)
    return response.text


# Learning Roadmap
def generate_learning_roadmap(resume_text: str, career_goal: str):
    prompt = f"""
Career Goal:
{career_goal}

Resume:
{resume_text}

Create a personalized 10-week learning roadmap.
"""

    response = model.generate_content(prompt)
    return response.text


# AI Chatbot
def chatbot_response(question: str):
    prompt = f"""
You are CareerPilot AI.

Answer this career question:

{question}
"""

    response = model.generate_content(prompt)
    return response.text