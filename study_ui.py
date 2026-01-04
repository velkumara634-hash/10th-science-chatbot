import streamlit as st
from hybrid.study_plan import generate_study_plan

def study_ui():
    st.header("📅 Study Planner")

    chapter = st.text_input("Chapter name", "Light")
    days = st.slider("Days", 1, 30, 7)

    if st.button("Generate Plan"):
        plan = generate_study_plan(chapter, days)

        for day, topics in plan.items():
            st.subheader(day)
            for t in topics:
                st.write("•", t)
