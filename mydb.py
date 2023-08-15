import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Kartikey@123'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE DB1")

print("All Done!")