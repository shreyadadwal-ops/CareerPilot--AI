import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/login"

def show_login():

    st.header("🔐 Login")

    email = st.text_input("Email")

    password = st.text_input("Password", type="password")

    if st.button("Login"):

        data = {
            "email": email,
            "password": password
        }

        response = requests.post(API_URL, json=data)

        if response.status_code == 200:

            result = response.json()

            st.success("Login Successful ✅")

            st.session_state["token"] = result["access_token"]
            st.session_state["logged_in"] = True

        else:
            st.error("Invalid Email or Password")