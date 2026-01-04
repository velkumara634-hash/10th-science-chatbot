import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

from ui.sidebar import sidebar
from ui.chat_ui import chat_ui
from ui.study_ui import study_ui
from ui.quiz_ui import quiz_ui
from ui.graph_ui import graph_ui
from ui.progress_ui import progress_ui

vectordb = Chroma(
    persist_directory="vector_store",
    embedding_function=OpenAIEmbeddings()
)

page = sidebar()

if page == "Chat Tutor":
    chat_ui(vectordb)

elif page == "Study Plan":
    study_ui()

elif page == "Quiz":
    quiz_ui(vectordb)

elif page == "Knowledge Graph":
    graph_ui()

elif page == "Progress":
    progress_ui()
