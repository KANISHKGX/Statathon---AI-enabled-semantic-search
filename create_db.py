import sqlite3

conn = sqlite3.connect("nco.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE occupations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nco_code TEXT,
    title TEXT,
    description TEXT
)
""")

cursor.execute("""
CREATE TABLE logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    query TEXT,
    result_code TEXT,
    confidence REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

cursor.execute("""
CREATE TABLE synonyms (
    word TEXT,
    synonym TEXT
)
""")

conn.commit()
conn.close()

print("New clean DB created!")
