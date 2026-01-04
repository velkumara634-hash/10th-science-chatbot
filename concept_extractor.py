from langchain_openai import ChatOpenAI
import json

llm = ChatOpenAI(temperature=0)

def extract_structure(text):
    prompt = f"""
From the text below, extract:
- chapter
- concepts (list)
- formulas (list, if any)

Return STRICT JSON only.

TEXT:
{text[:2000]}
"""
    response = llm.invoke(prompt)
    return json.loads(response.content)
