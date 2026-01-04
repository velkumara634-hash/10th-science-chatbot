import streamlit as st
from pyvis.network import Network
from kg.neo4j_driver import get_driver
import tempfile
import os

def graph_ui():
    st.header("🧠 Knowledge Graph")

    driver = get_driver()

    net = Network(height="600px", width="100%", bgcolor="#ffffff")

    with driver.session() as session:
        result = session.run("""
            MATCH (c:Chapter)-[:HAS_CONCEPT]->(k:Concept)
            RETURN c.name AS chapter, k.name AS concept
        """)

        for r in result:
            net.add_node(r["chapter"], label=r["chapter"], color="orange")
            net.add_node(r["concept"], label=r["concept"], color="lightblue")
            net.add_edge(r["chapter"], r["concept"])

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".html")
    net.save_graph(tmp.name)

    with open(tmp.name, "r", encoding="utf-8") as f:
        html = f.read()

    st.components.v1.html(html, height=650)
