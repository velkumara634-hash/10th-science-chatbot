# 📘 10th Std Science AI Tutor (RAG + Knowledge Graph)

An AI-powered tutor designed for **10th Standard Science students**, built using
**Retrieval-Augmented Generation (RAG)**, **Knowledge Graphs (Neo4j)**, and **student memory**.

This system goes beyond simple Q&A by understanding **syllabus structure**, tracking **student progress**, generating **study plans**, and visualizing concepts using a **graph-based approach**.

---

## 🚀 Features

### 1. Syllabus-Aware Chat Tutor
- Answers strictly from uploaded 10th Std Science textbooks
- Refuses out-of-syllabus questions
- Explains concepts in student-friendly language

### 2. Hybrid RAG Architecture
- **Vector DB (Chroma)** → retrieves relevant textbook content
- **Knowledge Graph (Neo4j)** → understands chapters, concepts & relationships
- **LLM** → generates grounded, accurate responses

### 3. Knowledge Graph Visualization
- Visual graph of:
  - Chapters → Concepts
  - Concept relationships
- Helps students *see* the syllabus structure

### 4. Study Plan Generator
- Creates day-wise study plans
- Uses concept structure from the Knowledge Graph
- Can adapt based on weak areas (future-ready)

### 5. Quiz Generator
- Generates MCQs directly from textbook content
- Avoids hallucinated questions
- Supports concept-based quizzes

### 6. Student Memory & Progress Tracking
- Tracks weak and strong concepts
- Enables revision-focused learning
- Stored in Neo4j for long-term memory

---

## 🧠 System Architecture

PDF Textbooks
↓
Vector DB (Chroma) ──┐
├── Hybrid RAG ── LLM ── Answer / Quiz / Plan
Knowledge Graph ─────┘
↓
Neo4j (Concepts, Progress, Memory)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI
- **LangChain (modern LCEL style)**
- **ChromaDB** – Vector database
- **Neo4j** – Knowledge Graph & student memory
- **OpenAI API** – Language model

---

## 📂 Project Structure

science_bot/
├── data/
│ └── pdf/ # 10th Std Science PDFs
├── rag/ # Vector DB pipeline
├── kg/ # Knowledge Graph (Neo4j)
├── hybrid/ # Hybrid RAG logic
├── memory/ # Student memory
├── ui/ # Streamlit UI modules
├── app.py # Main app
├── phase1_build.py # One-time vector indexing
└── .env

---

## ⚙️ Setup Instructions

### 1. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Set environment variables (.env)
env
Copy code
OPENAI_API_KEY=your_api_key
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=password
4. Start Neo4j
Using Neo4j Desktop or Docker

Ensure http://localhost:7474 opens

🧱 One-Time Indexing (IMPORTANT)
Run only once (or when PDFs change):

bash
Copy code
python phase1_build.py
This creates the Vector DB.

▶️ Run the Application
bash
Copy code
streamlit run app.py
🧪 Example Questions
Explain refraction of light

Create a quiz on reflection

Make a 7-day study plan for Light chapter

What concepts are related to refraction?

What should I revise today?

🎯 Project Goal
To demonstrate how AI + structured knowledge can be used to build
a real educational tutor, not just a chatbot.

📌 Future Enhancements
Adaptive quiz difficulty

Exam-pattern intelligence

Web search fallback (controlled)

Deployment (Docker / Cloud)

👨‍💻 Author
Built as a hands-on learning project to understand:

RAG systems

Knowledge Graphs

AI system design

yaml
Copy code

---

# 🎤 DEMO SCRIPT (WHAT YOU SAY WHILE SHOWING)

Use this **verbatim** or adapt slightly.  
This is designed so you sound **confident and logical**, not rehearsed.

---

### 🔹 1. Project Introduction (30 seconds)

> “This is a 10th Standard Science AI Tutor.  
> Unlike normal chatbots, it does not answer from the internet.  
> It answers strictly from the textbook using a combination of Vector Database and Knowledge Graph.”

---

### 🔹 2. Explain the Core Idea (30 seconds)

> “The system has two brains:
> one for **content retrieval** using embeddings,  
> and one for **understanding structure** using a Knowledge Graph in Neo4j.”

---

### 🔹 3. Show Chat Tutor

Ask:
Explain refraction of light

vbnet
Copy code

Say:
> “This answer is retrieved from the textbook, not generated randomly.”

Then ask:
Explain black holes

yaml
Copy code

Say:
> “The bot refuses because it’s out of syllabus. This is intentional.”

---

### 🔹 4. Show Knowledge Graph (MOST IMPACTFUL)

Open **Knowledge Graph tab**.

Say:
> “This is the syllabus visualized as a graph.  
> Chapters are connected to concepts.  
> This allows the system to understand dependencies.”

Zoom and click nodes.

---

### 🔹 5. Show Study Plan

Ask:
Create a study plan for Light chapter in 7 days

yaml
Copy code

Say:
> “The plan is generated using the concept structure from the graph.”

---

### 🔹 6. Show Quiz Generation

Ask:
Create a quiz on refraction

yaml
Copy code

Say:
> “Questions are generated strictly from the textbook content.”

---

### 🔹 7. Show Progress (if available)

Open **Progress tab**.

Say:
> “The system can track weak areas and suggest what to revise next.”

---

### 🔹 8. Close Strong (IMPORTANT)

> “This project shows how AI can be used responsibly in education,  
> combining retrieval, structure, and memory — not just chat.”