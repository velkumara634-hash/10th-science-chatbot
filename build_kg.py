from kg.neo4j_driver import get_driver
from kg.concept_extractor import extract_structure
from rag.pdf_loader import load_all_pdfs

def build_kg():
    driver = get_driver()
    docs = load_all_pdfs("data/pdf")

    with driver.session() as session:
        for doc in docs:
            try:
                data = extract_structure(doc.page_content)
            except Exception:
                continue

            chapter = data.get("chapter", "Unknown")

            session.run(
                "MERGE (c:Chapter {name:$name})",
                name=chapter
            )

            session.run("""
                MATCH (s:Subject {name:'10th Science'})
                MATCH (c:Chapter {name:$chapter})
                MERGE (s)-[:HAS_CHAPTER]->(c)
            """, chapter=chapter)

            for concept in data.get("concepts", []):
                session.run("""
                    MATCH (c:Chapter {name:$chapter})
                    MERGE (k:Concept {name:$concept})
                    MERGE (c)-[:HAS_CONCEPT]->(k)
                """, chapter=chapter, concept=concept)

            for formula in data.get("formulas", []):
                session.run("""
                    MATCH (k:Concept {name:$concept})
                    MERGE (f:Formula {expression:$formula})
                    MERGE (k)-[:USES_FORMULA]->(f)
                """, concept=data.get("concepts", [None])[0], formula=formula)

if __name__ == "__main__":
    build_kg()
    print("✅ Knowledge Graph built")
