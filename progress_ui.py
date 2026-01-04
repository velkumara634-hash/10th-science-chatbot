import streamlit as st
from memory.student_memory import get_weak_concepts

def progress_ui():
    st.header("📊 Learning Progress")

    weak = get_weak_concepts("default")

    if not weak:
        st.success("No weak concepts detected 🎉")
    else:
        st.warning("Focus on these concepts:")
        for c in weak:
            st.write("•", c)
