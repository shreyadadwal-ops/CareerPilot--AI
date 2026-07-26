# CareerPilot--AI
AI-powered Personalized Career Guidance Platform
# 🚀 CareerPilot AI

## 📌 Project Overview

CareerPilot AI is an AI-powered career guidance platform designed to help students make informed career decisions. The platform provides personalized career recommendations through resume analysis, skill gap detection, AI-powered career guidance, and learning roadmaps.

This project combines Artificial Intelligence with modern web technologies to assist students in planning and improving their professional journey.

---

# 🎯 Problem Statement

Many students struggle to identify the right career path, understand the skills required for their dream job, and receive personalized career guidance.

CareerPilot AI solves this problem by providing AI-based career assistance through resume analysis, career recommendations, and personalized learning suggestions.

---

# ✨ Features

- 👤 Student Registration
- 🔐 Secure Login Authentication (JWT)
- 📝 Student Profile Management
- 📄 Resume Upload
- 🤖 AI Resume Analysis
- 🎯 Skill Gap Analysis
- 🛣 Personalized Learning Roadmap
- 📊 Career Dashboard
- 💬 AI Career Chatbot

---

# 🛠 Tech Stack

### Frontend
- Streamlit

### Backend
- FastAPI

### Database
- SQLite
- SQLAlchemy

### Authentication
- JWT Authentication
- Bcrypt Password Hashing

### AI
- Google Gemini API

### Programming Language
- Python

---

# 📂 Project Structure

```
CareerPilot--AI
│
├── backend
│   ├── models
│   ├── routes
│   ├── schemas
│   ├── services
│   ├── uploads
│   ├── database.py
│   ├── crud.py
│   └── main.py
│
├── frontend
│   ├── assets
│   ├── app.py
│   ├── register.py
│   ├── login.py
│   ├── profile.py
│   ├── resume.py
│   ├── dashboard.py
│   ├── chatbot.py
│   └── style.py
│
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/shreyadadwal-ops/CareerPilot--AI.git
```

## Open Project

```bash
cd CareerPilot--AI
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Backend

```bash
uvicorn backend.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

API Documentation

```
http://127.0.0.1:8000/docs
```

---

# ▶ Running the Frontend

```bash
streamlit run frontend/app.py
```

---

# 🚀 Workflow

1. Register a new account.
2. Login securely.
3. Complete your student profile.
4. Upload your resume.
5. Receive AI-powered resume analysis.
6. View skill gap analysis.
7. Access your career dashboard.
8. Interact with the AI Career Chatbot.

---

# 📈 Future Enhancements

- ATS Resume Scoring
- AI Interview Preparation
- Internship Recommendations
- Job Recommendation System
- Career Progress Tracking
- Resume Templates
- Admin Dashboard
- Email Notifications

---

# 👥 Team Members

- Shreya Dadwal
- Team Member 2
- Team Member 3

---

# 📜 License

This project is developed for educational and MVP demonstration purposes.

---

# ⭐ Acknowledgements

- FastAPI
- Streamlit
- SQLAlchemy
- Google Gemini AI
- Python Community
