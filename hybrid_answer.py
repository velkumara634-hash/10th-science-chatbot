from langchain_openai import ChatOpenAI
from kg.neo4j_driver import get_driver

llm = ChatOpenAI(temperature=0)

def get_related_concepts(question):
    driver = get_driver()
    with driver.session() as session:
        result = session.run("""
            MATCH (c:Concept)
            WHERE toLower(c.name) CONTAINS toLower($q)
            RETURN c.name LIMIT 5
        """, q=question)
        return [r["c.name"] for r in result]

def hybrid_answer(question, vectordb):
    docs = vectordb.similarity_search(question, k=4)
    context = "\n".join(d.page_content for d in docs)

    concepts = get_related_concepts(question)
    concepts_text = ", ".join(concepts) if concepts else "None"

    prompt = f"""
You are a 10th standard science teacher.

Use ONLY the given context.
If not found, say "Out of syllabus".

Context:
{context}

Related Concepts:
{concepts_text}

Question:
{question}
"""
    return llm.invoke(prompt).content
