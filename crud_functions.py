import sqlite3

# connection = sqlite3.connect("not_telegram.db")
# cursor = connection.cursor()


async def initiate_db():
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        pic TEXT NOT NULL,
        price INTEGER NOT NULL
        )
    
    ''')
    cursor.execute("DELETE FROM Products WHERE id IS NOT NULL")

    for i in range(4):
        cursor.execute("INSERT INTO Products(title,description,price, pic) VALUES(?, ?, ?, ?)",(f"Продукт {i+1}",f"Описание {i+1}",f"{(i+1)*100}", f"image_{i+1}.jpg"))
    connection.commit()
    connection.close()
async def get_all_products():
    pass
    connection = sqlite3.connect("not_telegram.db")
    cursor = connection.cursor()

    cursor.execute("SELECT title,description,price,pic FROM Products")
    rows = cursor.fetchall()
    return rows
    # for row in rows:
    #     print(f"Имя:{row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")
    connection.commit()
    connection.close()
