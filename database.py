import sqlite3 as sql

def create_table():
    conn = sql.connect('ogrenci.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS USERS(
        id integer PRIMARY KEY,
        ogrenci text,
        kitap text,
        tarih text
    ) """)

    conn.commit()
    conn.close()

def insert(ogrenci, kitap, tarih):
    conn = sql.connect('ogrenci.db')
    cursor = conn.cursor()

    add_command = """INSERT INTO USERS(ogrenci, kitap, tarih) VALUES {} """
    data = (ogrenci, kitap, tarih)

    cursor.execute(add_command.format(data))

    conn.commit()
    conn.close()

def print_all():
    conn = sql.connect('ogrenci.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT * from USERS""")
    list_all = cursor.fetchall()

    conn.close()
    return list_all



