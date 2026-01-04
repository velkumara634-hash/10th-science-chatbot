from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def create_vectordb(chunks):
    embeddings = OpenAIEmbeddings()

    vectordb = Chroma.from_documents(
        chunks,
        embedding=embeddings,
        persist_directory="vector_store"
    )

    vectordb.persist()
