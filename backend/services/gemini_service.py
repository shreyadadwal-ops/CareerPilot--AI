import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()
print("Gemini API Key:", os.getenv("GEMINI_API_KEY"))

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini Model
model = genai.GenerativeModel("gemini-1.5-flash")


# -----------------------------
# Career Recommendation
# -----------------------------
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


# -----------------------------
# Resume Analysis
# -----------------------------
def analyze_resume(resume_text: str):
    try:
        prompt = f"""
You are an expert resume reviewer.

Analyze this resume.

Resume:

{resume_text}

Return:
1. Resume Score
2. Strengths
3. Weaknesses
4. Missing Skills
5. Recommended Careers
6. Recommended Courses
"""

        response = model.generate_content(prompt)
        print("Gemini Response:", response.text)
        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        raise e


# -----------------------------
# Skill Gap Analysis
# -----------------------------
def skill_gap_analysis(resume_text: str):
    prompt = f"""
Analyze this resume.

Resume:

{resume_text}

Provide:

1. Current Skills

2. Missing Skills

3. Recommended Skills

4. Best Online Courses

5. Estimated Learning Time
"""

    response = model.generate_content(prompt)
    return response.text


# -----------------------------
# Learning Roadmap
# -----------------------------
def generate_learning_roadmap(resume_text: str):
    prompt = f"""
You are an expert career mentor.

Analyze the following resume.

Resume:

{resume_text}

Identify the most suitable career path.

Then create a detailed personalized 10-week roadmap.

Include:

Week 1-2

Week 3-4

Week 5-6

Week 7-8

Week 9-10

Also provide:

• Certifications

• Projects

• Interview Preparation

• Useful Resources
"""

    response = model.generate_content(prompt)
    return response.text


# -----------------------------
# AI Chatbot
# -----------------------------
def chatbot_response(question: str):
    prompt = f"""
You are CareerPilot AI.

Answer the following career-related question.

Question:

{question}
"""

    response = model.generate_content(prompt)
    return response.text