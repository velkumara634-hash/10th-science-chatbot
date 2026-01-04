from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)

def generate_quiz(concept, vectordb):
    docs = vectordb.similarity_search(concept, k=2)
    context = docs[0].page_content

    prompt = f"""
Create 10 MCQs strictly from the content below.
Include answers.

Content:
{context}
"""
    return llm.invoke(prompt).content
