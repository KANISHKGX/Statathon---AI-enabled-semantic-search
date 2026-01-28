import sqlite3
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load data from DB
conn = sqlite3.connect("nco.db")
cursor = conn.cursor()

rows = cursor.execute("""
SELECT id, title, description FROM occupations
""").fetchall()

print(f"Loaded {len(rows)} occupations")

texts = []
ids = []

for r in rows:
    ids.append(r[0])

    title = r[1] or ""
    desc = r[2] or ""

    texts.append(title + " " + desc)


print("Generating embeddings...")
embeddings = model.encode(texts, show_progress_bar=True)

embeddings = np.array(embeddings).astype("float32")

dim = embeddings.shape[1]

print("Building FAISS index...")
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

faiss.write_index(index, "faiss.index")

# Save ID mapping
np.save("id_map.npy", np.array(ids))

print("FAISS index built successfully!")
