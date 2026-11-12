import sqlite3
import pandas as pd

conn = sqlite3.connect("school.db")
conn.execute("DROP TABLE IF EXISTS Student")
conn.execute("""
CREATE TABLE Student (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL UNIQUE,
    Age INTEGER,
    City TEXT DEFAULT 'Delhi'
);
""")

conn.execute("INSERT INTO Student VALUES (1, 'Rahul', 15, 'Jhansi')")
conn.execute("INSERT INTO Student VALUES (2, 'Nitish Alariya', 21, 'Chandigarh')")
conn.execute("INSERT INTO Student (ID, Name, Age) VALUES (3, 'Aman', 16) ")

conn.commit()

print("Student Records _-_-_-_-_")
print(pd.read_sql("SELECT * FROM Student", conn))

try:
    conn.execute("INSERT INTO Student VALUES (4, 'Rahul', 17, 'Delhi')")
    conn.commit()
except Exception as e:
    print("Error :", e)
    conn.rollback()

try:
    conn.execute("INSERT INTO Student VALUES (5, NULL, 15, 'Hathras')")
    conn.commit()
except Exception as e:
    print("Error :", e)
    conn.rollback()
    
conn.close