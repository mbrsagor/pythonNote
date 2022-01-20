import mysql.connector

db_string = mysql.connector.connect(
  host="localhost",
  user="root",
  password=12345678
)

print(db_string)
