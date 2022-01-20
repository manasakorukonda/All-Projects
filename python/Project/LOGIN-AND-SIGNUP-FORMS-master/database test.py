import sqlite3

def createTable():
    conn = sqlite3.connect("login.db")

    #conn.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL,EMAIL TEXT,PASSWORD TEXT NOT NULL)")

    conn.execute("INSERT INTO USERS VALUES(?,?,?)",('MANASA','ravimanasa098@gmail.com','Manu@1997'))

    conn.commit()

    result= conn.execute("SELECT * FROM USERS")

    for data in result:
        print("userName: ",data[0])
        print("Email: ",data[1])
        print("Password: ",data[2])
    conn.close()

createTable()
    
    
                 
