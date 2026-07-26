import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/login"


def show_login():

    st.markdown(
        "<h1 style='color:white;'>🔐 Login</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='color:white;font-size:18px;'>Login to your CareerPilot AI account</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h4 style='color:white;'>Email</h4>",
        unsafe_allow_html=True
    )
    email = st.text_input("", key="login_email")

    st.markdown(
        "<h4 style='color:white;'>Password</h4>",
        unsafe_allow_html=True
    )
    password = st.text_input(
        "",
        type="password",
        key="login_password"
    )

    if st.button("Login"):

        data = {
            "email": email,
            "password": password
        }

        response = requests.post(
            API_URL,
            json=data
        )

        if response.status_code == 200:

            result = response.json()

            st.success("✅ Login Successful!")

            st.session_state["token"] = result["access_token"]
            st.session_state["logged_in"] = True

        else:
            st.error("❌ Invalid Email or Password")