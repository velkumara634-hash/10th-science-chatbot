import streamlit as st
from hybrid.intent_router import detect_intent
from hybrid.hybrid_answer import hybrid_answer
from hybrid.study_plan import generate_study_plan
from hybrid.quiz_engine import generate_quiz

def chat_ui(vectordb):
    st.header("💬 Chat Tutor")

    query = st.text_input("Ask from syllabus")

    if st.button("Ask"):
        intent = detect_intent(query)

        if intent == "STUDY_PLAN":
            response = generate_study_plan("Light", 7)
        elif intent == "QUIZ":
            response = generate_quiz(query, vectordb)
        else:
            response = hybrid_answer(query, vectordb)

        st.write(response)
