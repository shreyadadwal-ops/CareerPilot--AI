import streamlit as st

def show_chatbot():

    st.header("🤖 AI Career Chatbot")

    question = st.text_input("Ask a career question")

    if st.button("Ask"):

        if question:
            st.write("AI Response will appear here.")

        else:
            st.warning("Please enter a question.")