import psycopg2

conn = psycopg2.connect(database="dev", host="localhost", user="sagor", password="12345", port=5432)

cursor = conn.cursor()

print(cursor.fetchall())
