from fastapi import FastAPI
import duckdb
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

app = FastAPI()

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading FAISS index...")
index = faiss.read_index("data/faiss.index")

print("Loading database...")
conn = duckdb.connect(
    "data/support.duckdb",
    read_only=True
)

df = conn.execute("""
SELECT clean_text
FROM processed_data
LIMIT 100
""").fetchdf()

@app.get("/")
def home():
    return {"message": "Semantic Search API Running"}

@app.get("/search")
def search(query: str, k: int = 5):

    query_embedding = model.encode([query]).astype("float32")

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for i in indices[0]:
        results.append(df.iloc[i]["clean_text"])

    return {
        "query": query,
        "results": results
    }