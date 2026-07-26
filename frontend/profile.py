import streamlit as st


def show_profile():

    st.markdown(
        "<h1 style='color:white;'>👤 Student Profile</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='color:white;font-size:18px;'>Complete your profile to receive personalized career recommendations.</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h4 style='color:white;'>Full Name</h4>",
        unsafe_allow_html=True
    )
    name = st.text_input("", key="profile_name")

    st.markdown(
        "<h4 style='color:white;'>Email</h4>",
        unsafe_allow_html=True
    )
    email = st.text_input("", key="profile_email")

    st.markdown(
        "<h4 style='color:white;'>College</h4>",
        unsafe_allow_html=True
    )
    college = st.text_input("", key="profile_college")

    st.markdown(
        "<h4 style='color:white;'>Degree</h4>",
        unsafe_allow_html=True
    )
    degree = st.text_input("", key="profile_degree")

    st.markdown(
        "<h4 style='color:white;'>Skills</h4>",
        unsafe_allow_html=True
    )
    skills = st.text_area("", key="profile_skills")

    st.markdown(
        "<h4 style='color:white;'>Career Goal</h4>",
        unsafe_allow_html=True
    )
    career_goal = st.text_input("", key="profile_goal")

    if st.button("Save Profile"):
        st.success("✅ Profile saved successfully!")