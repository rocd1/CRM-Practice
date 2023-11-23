import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'edoria16'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE djacrm")

print("All Done!")