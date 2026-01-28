import faiss
import numpy as np
import sqlite3
from sentence_transformers import SentenceTransformer

print("Loading model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading FAISS index...")
index = faiss.read_index("faiss.index")
id_map = np.load("id_map.npy")

conn = sqlite3.connect("nco.db")
cursor = conn.cursor()

def search(query, k=5):
    print(f"\nSearching for: {query}")

    q_vec = model.encode([query]).astype("float32")

    D, I = index.search(q_vec, k)

    for idx in I[0]:
        row_id = id_map[idx]

        row = cursor.execute(
            "SELECT title FROM occupations WHERE id=?",
            (int(row_id),)
        ).fetchone()

        print("→", row[0])


# 🔥 TEST HERE
search("tailor stitching clothes")
search("drives truck")
search("teaches students")
