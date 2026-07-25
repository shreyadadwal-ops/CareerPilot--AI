import streamlit as st

def show_dashboard():

    st.header("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Skills Completed", "5")

    with col2:
        st.metric("Courses", "3")

    with col3:
        st.metric("Career Score", "85%")

    st.success("Welcome to your CareerPilot AI Dashboard!")