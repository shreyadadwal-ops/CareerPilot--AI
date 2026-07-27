import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/register"


def show_register():

    st.markdown(
        "<h1 style='color:white;'>📝 Register</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='color:white;font-size:18px;'>Create your CareerPilot AI account</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h4 style='color:white;'>Full Name</h4>",
        unsafe_allow_html=True
    )
    name = st.text_input("", key="register_name")

    st.markdown(
        "<h4 style='color:white;'>Email</h4>",
        unsafe_allow_html=True
    )
    email = st.text_input("", key="register_email")

    st.markdown(
        "<h4 style='color:white;'>Password</h4>",
        unsafe_allow_html=True
    )
    password = st.text_input(
        "",
        type="password",
        key="register_password"
    )

    if st.button("Register"):

        if not name or not email or not password:
            st.error("Please fill all fields.")

        else:

            data = {
                "username": name,
                "email": email,
                "password": password
            }

            response = requests.post(
                API_URL,
                json=data
            )

            if response.status_code == 200:
                st.success("✅ Registration Successful!")

            else:
                st.error(response.text)