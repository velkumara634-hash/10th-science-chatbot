from kg.neo4j_driver import get_driver

def generate_study_plan(chapter, days):
    driver = get_driver()
    with driver.session() as session:
        result = session.run("""
            MATCH (c:Chapter {name:$chapter})-[:HAS_CONCEPT]->(k:Concept)
            RETURN k.name
        """, chapter=chapter)

        concepts = [r["k.name"] for r in result]

    plan = {}
    per_day = max(1, len(concepts)//days)

    for i in range(days):
        plan[f"Day {i+1}"] = concepts[i*per_day:(i+1)*per_day]

    return plan
from memory.student_memory import get_weak_concepts

def adaptive_study_plan(student_id, chapter, days):
    weak = get_weak_concepts(student_id)

    if weak:
        return {
            "Focus Areas": weak,
            "Advice": "Revise weak concepts first before moving ahead"
        }

    return {
        "Plan": f"Study {chapter} evenly over {days} days"
    }
