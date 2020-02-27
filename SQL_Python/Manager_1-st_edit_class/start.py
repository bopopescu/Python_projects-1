import mysql.connector
from lib.manager import manager
from lib.manager import Db_manager

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="loginsystem"
# )
# cursor = db.cursor()

# cursor.execute("SHOW TABLES")
# for item in cursor:
#   print(item)

# sql = "INSERT INTO users (name, surname, age, email) VALUES (%s, %s, %s, %s)"
# value = (name, surname, age, email)

# cursor.execute(sql, value)
# db.commit()
# print(cursor.rowcount, "record inserted.")

# cursor.execute("SELECT name, surname, age, email FROM users")

# result = cursor.fetchall()
# result = cursor.fetchone()

# for item in result:
#     print(item)
# cursor.execute("ADD password VARCHAR")
#------------------------------
manager()

