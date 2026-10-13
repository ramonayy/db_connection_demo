import mysql.connector


try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="cuckoo5192#",
        database="company"
    )
    print(mydb)

    cursor = mydb.cursor()
    cursor.execute("SELECT VName, Nname FROM Angestellter")

    rows = cursor.fetchall()
    print(rows)

except mysql.connector.Error as err:
    print(f"Fehler: {err}")
finally:
    # Der finally-Block wird IMMER ausgeführt
    if mydb and mydb.is_connected():
        cursor.close()
        mydb.close()
        print("MySQL-Verbindung erfolgreich geschlossen.")
