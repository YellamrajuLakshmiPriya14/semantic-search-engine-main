import numpy as np
import faiss

print("Loading embeddings...")

# Load embeddings
embeddings = np.load("data/embeddings.npy")

print("Shape:", embeddings.shape)

# FAISS requires float32
embeddings = embeddings.astype("float32")

# Get vector dimension
dimension = embeddings.shape[1]

# Create index
index = faiss.IndexFlatL2(dimension)

# Add vectors
index.add(embeddings)

print("Vectors added:", index.ntotal)

# Save index
faiss.write_index(index, "data/faiss.index")

print("FAISS index created successfully!")