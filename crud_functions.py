import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        pic TEXT NOT NULL,
        price INTEGER NOT NULL
        )
    
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INT NOT NULL,
        balance INTEGER NOT NULL
        )

    ''')

    cursor.execute("DELETE FROM Products WHERE id IS NOT NULL")

    for i in range(4):
        cursor.execute("INSERT INTO Products(title,description,price, pic) VALUES(?, ?, ?, ?)",(f"Продукт {i+1}",f"Описание {i+1}",f"{(i+1)*100}", f"image_{i+1}.jpg"))
    connection.commit()
def add_user(username,email,age,balance):

    cursor.execute("INSERT INTO Users(username,email,age,balance) VALUES(?, ?, ?, ?)", (username,email,age,balance))
    connection.commit()

def is_included(username):
    cursor.execute("SELECT COUNT(*) FROM Users")
    count = cursor.fetchone()[0]
    if count != 0:
        cursor.execute("SELECT COUNT(*) FROM Users WHERE username = ?",(username,))
        count_us = cursor.fetchone()[0]
    else:
        return False
    if count_us != 0:
        return True
    else:
        return False
def get_all_products():

    cursor.execute("SELECT title,description,price,pic FROM Products")
    rows = cursor.fetchall()
    return rows
def is_latin(word):
    return word.isalpha() and word.isascii()

