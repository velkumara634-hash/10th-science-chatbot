from dotenv import load_dotenv
load_dotenv()

from rag.pdf_loader import load_all_pdfs
from rag.chunker import chunk_docs
from rag.vector_db import create_vectordb


docs = load_all_pdfs("data/pdf")
print(f"Loaded {len(docs)} pages")

chunks = chunk_docs(docs)
print(f"Created {len(chunks)} chunks")

create_vectordb(chunks)

print("✅ One-time indexing completed")
print(docs[0].page_content[:300])
    