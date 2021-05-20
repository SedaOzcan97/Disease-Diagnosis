import sqlite3

def createTable():
    connection = sqlite3.connect("login.db")

    result = connection.execute("SELECT * FROM USERS")

    for data in result:
        print("Username: ",data[0])
        print("Email: ",data[1])
        print("Password:",data[2])

    connection.close()

createTable()
