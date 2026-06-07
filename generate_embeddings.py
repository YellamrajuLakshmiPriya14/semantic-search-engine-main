import duckdb
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect database
conn = duckdb.connect("data/support.duckdb")

# Read only 100 rows
df = conn.execute("""
SELECT clean_text
FROM processed_data
LIMIT 100
""").fetchdf()

texts = df["clean_text"].tolist()

print("Generating embeddings...")

embeddings = model.encode(texts)

print("Embedding shape:", embeddings.shape)

# Save embeddings
np.save("data/embeddings.npy", embeddings)

print("Embeddings saved successfully!")