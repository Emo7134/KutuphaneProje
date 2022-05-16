import sqlite3 as sql

def create_table():
    conn = sql.connect('kitap.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS(
        id integer PRIMARY KEY,
        kitap text,
        yazar text
    ) """)

    conn.commit()
    conn.close()

def insert(kitap, yazar):
    conn = sql.connect('kitap.db')
    cursor = conn.cursor()

    add_command = """INSERT INTO USERS(kitap, yazar) VALUES {} """
    data = (kitap, yazar)

    cursor.execute(add_command.format(data))

    conn.commit()
    conn.close()

def print_all():
    conn = sql.connect('kitap.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT * from USERS""")
    list_all = cursor.fetchall()

    conn.close()
    return list_all