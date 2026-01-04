from kg.neo4j_driver import get_driver

def init_student(student_id="default"):
    driver = get_driver()
    with driver.session() as session:
        session.run("""
            MERGE (s:Student {id:$id})
        """, id=student_id)

def update_progress(student_id, concept, score):
    driver = get_driver()
    mastery = "STRONG" if score >= 80 else "WEAK"

    with driver.session() as session:
        session.run("""
            MATCH (s:Student {id:$id})
            MERGE (p:Progress {concept:$concept})
            SET p.mastery = $mastery, p.score = $score
            MERGE (s)-[:HAS_PROGRESS]->(p)
        """, id=student_id, concept=concept, mastery=mastery, score=score)

def get_weak_concepts(student_id):
    driver = get_driver()
    with driver.session() as session:
        result = session.run("""
            MATCH (s:Student {id:$id})-[:HAS_PROGRESS]->(p:Progress)
            WHERE p.mastery = 'WEAK'
            RETURN p.concept
        """, id=student_id)

        return [r["p.concept"] for r in result]
