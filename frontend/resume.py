import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/upload-resume"


def show_resume():

    st.markdown(
        "<h1 style='color:white;'>📄 Resume Analysis</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='color:white;font-size:18px;'>Upload your resume and receive AI-powered analysis with skill gap recommendations.</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h4 style='color:white;'>Upload your Resume (PDF)</h4>",
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"],
        key="resume_upload",
        label_visibility="collapsed"
    )

    if uploaded_file is not None:

        st.success(f"✅ Selected: {uploaded_file.name}")

        if st.button("Analyze Resume"):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "application/pdf"
                )
            }

            response = requests.post(API_URL, files=files)

            if response.status_code == 200:

                result = response.json()

                st.success(result["message"])

                # Resume Analysis
                st.markdown(
                    "<h3 style='color:white;'>📄 Resume Analysis</h3>",
                    unsafe_allow_html=True
                )
                st.write(result["resume_analysis"])

                # Skill Gap Analysis
                st.markdown(
                    "<h3 style='color:white;'>🎯 Skill Gap Analysis</h3>",
                    unsafe_allow_html=True
                )
                st.write(result["skill_gap_analysis"])

                # Learning Roadmap
                st.markdown(
                    "<h3 style='color:white;'>🗺️ Personalized Learning Roadmap</h3>",
                    unsafe_allow_html=True
                )
                st.write(result["learning_roadmap"])

            else:
                st.error(response.text)