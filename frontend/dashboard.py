import streamlit as st


def show_dashboard():

    st.markdown(
        "<h1 style='color:white;'>📊 Dashboard</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='color:white;font-size:18px;'>Welcome to your personalized CareerPilot AI Dashboard.</p>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="🎯 Skills Completed",
            value="5"
        )

    with col2:
        st.metric(
            label="📚 Courses Completed",
            value="3"
        )

    with col3:
        st.metric(
            label="📈 Career Score",
            value="85%"
        )

    st.markdown("---")

    st.success("✅ Welcome to your CareerPilot AI Dashboard!")

    st.info(
        """
        **Your Dashboard helps you:**

        • 📄 Track your Resume Analysis

        • 🎯 View Skill Gap Analysis

        • 📚 Monitor your Learning Progress

        • 🤖 Get AI Career Recommendations
        """
    )