import streamlit as st
from hybrid.quiz_engine import generate_quiz

def quiz_ui(vectordb):
    st.header("📝 Quiz")

    concept = st.text_input("Enter concept")

    if st.button("Generate Quiz"):
        quiz = generate_quiz(concept, vectordb)
        st.write(quiz)
