import streamlit as st

def sidebar():
    st.sidebar.title("📘 10th Std Science AI Tutor")

    page = st.sidebar.radio(
        "Navigate",
        [
            "Chat Tutor",
            "Study Plan",
            "Quiz",
            "Knowledge Graph",
            "Progress"
        ]
    )

    return page
