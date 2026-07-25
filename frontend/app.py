import streamlit as st

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide"
)

from style import add_bg_and_css
add_bg_and_css()

from register import show_register
from login import show_login
from profile import show_profile
from dashboard import show_dashboard
from chatbot import show_chatbot
from resume import show_resume

st.sidebar.title("CareerPilot AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Register",
        "Login",
        "Profile",
        "Resume",
        "Dashboard",
        "Chatbot"
    ]
)

if page == "Home":

    st.markdown("""
    <style>
    .hero{
        background: linear-gradient(135deg,#0F172A,#1E3A8A,#2563EB);
        padding:40px;
        border-radius:18px;
        color:white;
        text-align:center;
        margin-bottom:25px;
    }

    .feature{
        background:#F8FAFC;
        border-left:6px solid #2563EB;
        padding:18px;
        border-radius:12px;
        margin-bottom:15px;
        box-shadow:0px 2px 8px rgba(0,0,0,0.08);
    }

    .stat{
        background:#111827;
        color:white;
        padding:20px;
        border-radius:15px;
        text-align:center;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
        <h1>🚀 CareerPilot AI</h1>
        <h3>AI-Powered Career Guidance & Resume Intelligence Platform</h3>
        <p>
        Helping students discover career paths using Artificial Intelligence,
        Resume Analysis, Skill Gap Detection, Personalized Learning Roadmaps,
        and an AI Career Assistant.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1,col2,col3,col4=st.columns(4)

    with col1:
        st.metric("👨‍🎓 Students","1000+")

    with col2:
        st.metric("📄 Resume Reviews","2500+")

    with col3:
        st.metric("🤖 AI Suggestions","10000+")

    with col4:
        st.metric("🎯 Career Domains","50+")

    st.divider()

    st.subheader("⚡ Platform Features")

    c1,c2=st.columns(2)

    with c1:

        st.markdown("""
        <div class="feature">
        <h4>📄 AI Resume Analyzer</h4>
        Upload resumes and receive AI-powered analysis,
        ATS feedback and improvement suggestions.
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div class="feature">
        <h4>🎯 Skill Gap Analysis</h4>
        Identify missing technical and soft skills
        required for your target career.
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div class="feature">
        <h4>🛣 Personalized Roadmap</h4>
        Generate learning paths with courses,
        certifications and project recommendations.
        </div>
        """,unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="feature">
        <h4>🤖 AI Career Chatbot</h4>
        Ask career questions and receive
        intelligent AI guidance instantly.
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div class="feature">
        <h4>📊 Career Dashboard</h4>
        Track your progress, skills,
        achievements and career score.
        </div>
        """,unsafe_allow_html=True)

        st.markdown("""
        <div class="feature">
        <h4>👤 Student Profile</h4>
        Manage your education,
        skills and career preferences.
        </div>
        """,unsafe_allow_html=True)

    st.divider()

    st.subheader("🛠 Technology Stack")

    st.info("""
    **Frontend:** Streamlit

    **Backend:** FastAPI

    **Database:** SQLite + SQLAlchemy

    **Authentication:** JWT + Bcrypt

    **AI Engine:** Google Gemini

    **Language:** Python
    """)

    st.success("🚀 Welcome to CareerPilot AI — Build, Analyze and Accelerate Your Career with AI.")

    st.success("Frontend is working successfully!")

elif page == "Register":
    show_register()

elif page == "Login":
    show_login()

elif page == "Profile":
    show_profile()

elif page =="Resume":
    show_resume()

elif page == "Dashboard":
    show_dashboard()

elif page == "Chatbot":
    show_chatbot()