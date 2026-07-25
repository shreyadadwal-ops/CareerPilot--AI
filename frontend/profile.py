import streamlit as st

def show_profile():

    st.header("👤 Student Profile")

    name = st.text_input("Full Name")

    email = st.text_input("Email")

    college = st.text_input("College")

    degree = st.text_input("Degree")

    skills = st.text_area("Skills")

    career_goal = st.text_input("Career Goal")

    if st.button("Save Profile"):
        st.success("Profile saved successfully! ✅")