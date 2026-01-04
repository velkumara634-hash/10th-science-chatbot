from kg.neo4j_driver import get_driver

def create_schema():
    driver = get_driver()
    with driver.session() as session:
        session.run("MERGE (:Subject {name:'10th Science'})")
