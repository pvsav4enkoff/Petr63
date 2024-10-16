import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )

''')
cursor.execute("DELETE FROM users WHERE id IS NOT NULL")

for i in range(10):
    cursor.execute("INSERT INTO Users(username,email,age,balance) VALUES(?, ?, ?, ?)",(f"User{i+1}",f"example{i+1}@gmail.com",f"{(i+1)*10}",1000))

cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 != 0")

cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")

rows = cursor.fetchall()

for row in rows:
    print(f"Имя:{row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")

connection.commit()
connection.close()
