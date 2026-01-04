import os
from langchain_community.document_loaders import PyPDFLoader

def load_all_pdfs(folder_path):
    """
    Loads all PDFs from a folder and returns page-wise Documents
    """
    all_docs = []

    for file in os.listdir(folder_path):
        if file.lower().endswith(".pdf"):
            full_path = os.path.join(folder_path, file)
            loader = PyPDFLoader(full_path)
            all_docs.extend(loader.load())

    return all_docs
