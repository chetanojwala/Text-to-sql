import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    marks INTEGER
)
""")

cursor.execute("INSERT INTO students (name, marks) VALUES ('Rahul', 85)")
cursor.execute("INSERT INTO students (name, marks) VALUES ('Anjali', 92)")
cursor.execute("INSERT INTO students (name, marks) VALUES ('Kiran', 70)")
cursor.execute("INSERT INTO students (name, marks) VALUES ('Sneha', 88)")

conn.commit()
conn.close()

print("Database created successfully ✅")