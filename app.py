import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

print("📊 Text-to-SQL System")
print("Type your query (example: 'all students' or 'marks greater than 80')")
print("Type 'exit' to quit\n")

while True:
    query = input("Ask your question: ").lower()

    if query == "exit":
        print("Goodbye 👋")
        break

    if "all students" in query:
        sql = "SELECT * FROM students"

    elif "marks greater than" in query:
        try:
            number = int(query.split()[-1])
            sql = f"SELECT * FROM students WHERE marks > {number}"
        except:
            print("❌ Please enter a valid number")
            continue

    elif "top student" in query:
        sql = "SELECT * FROM students ORDER BY marks DESC LIMIT 1"

    elif "average marks" in query:
        sql = "SELECT AVG(marks) FROM students"

    else:
        print("❌ Sorry, I don't understand this query")
        continue

    print("\nGenerated SQL:", sql)

    cursor.execute(sql)
    results = cursor.fetchall()

    print("\n📌 Results:")
    for row in results:
        print(row)

    print("\n------------------------\n")

conn.close()