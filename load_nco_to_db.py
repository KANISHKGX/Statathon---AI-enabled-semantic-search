import sqlite3
import pandas as pd

df = pd.read_csv("data/nco_clean.csv")

print("CSV columns:", df.columns)

# Rename to match DB
df = df.rename(columns={
    "Code": "nco_code",
    "Title": "title",
    "Description": "description"
})

conn = sqlite3.connect("nco.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM occupations")

cursor.executemany("""
INSERT INTO occupations (nco_code, title, description)
VALUES (?, ?, ?)
""", df[["nco_code", "title", "description"]].values.tolist())

conn.commit()

count = cursor.execute("SELECT COUNT(*) FROM occupations").fetchone()[0]
print(f"Inserted {count} rows successfully!")

conn.close()
