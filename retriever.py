from dotenv import load_dotenv
load_dotenv()

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def get_qa_chain():
    embeddings = OpenAIEmbeddings()

    vectordb = Chroma(
        persist_directory="vector_store",
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    llm = ChatOpenAI(temperature=0)

    prompt = ChatPromptTemplate.from_template(
        """
        Answer ONLY from the context below.
        If the answer is not in the context, say "Out of syllabus".

        Context:
        {context}

        Question:
        {question}
        """
    )

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
