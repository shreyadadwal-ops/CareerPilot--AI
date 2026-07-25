import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/upload-resume"

def show_resume():

    st.header("📄 Resume Analysis")

    uploaded_file = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.success(f"Selected: {uploaded_file.name}")

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

                st.subheader("📄 Resume Analysis")
                st.write(result["resume_analysis"])

                st.subheader("🎯 Skill Gap Analysis")
                st.write(result["skill_gap_analysis"])

            else:
                st.error(response.text)