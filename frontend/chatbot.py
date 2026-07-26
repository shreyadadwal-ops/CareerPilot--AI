import streamlit as st


def show_chatbot():

    st.markdown(
        "<h1 style='color:white;'>🤖 AI Career Chatbot</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='color:white;font-size:18px;'>Ask CareerPilot AI any career-related question and receive AI-powered guidance.</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h4 style='color:white;'>Ask a Career Question</h4>",
        unsafe_allow_html=True
    )

    question = st.text_input(
        "",
        key="chatbot_question"
    )

    if st.button("Ask AI"):

        if question:

            st.success("✅ Question Submitted Successfully!")

            st.markdown(
                "<h3 style='color:white;'>🤖 AI Response</h3>",
                unsafe_allow_html=True
            )

            st.info("AI Response will appear here.")

        else:

            st.warning("⚠ Please enter a career-related question.")