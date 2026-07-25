import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/register"

def show_register():

    st.header("📝 Register")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):

        if not name or not email or not password:
            st.error("Please fill all fields.")

        else:

            data = {
                "username": name,
                "email": email,
                "password": password
            }

            response = requests.post(API_URL, json=data)

            if response.status_code == 200:
                st.success("Registration Successful ✅")

            else:
                st.error(response.text)