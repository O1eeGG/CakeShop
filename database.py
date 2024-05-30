import sqlite3

def init_db():
    conn = sqlite3.connect('cake_shop.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cakes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cake_id INTEGER,
            quantity INTEGER,
            total_price REAL,
            sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(cake_id) REFERENCES cakes(id)
        )
    ''')
    conn.commit()
    conn.close()

def add_cake(name, price, stock):
    conn = sqlite3.connect('cake_shop.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO cakes (name, price, stock) VALUES (?, ?, ?)', (name, price, stock))
    conn.commit()
    conn.close()

def list_cakes():
    conn = sqlite3.connect('cake_shop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, price, stock FROM cakes')
    cakes = cursor.fetchall()
    conn.close()
    return cakes

def sell_cake(cake_id, quantity):
    conn = sqlite3.connect('cake_shop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT price, stock FROM cakes WHERE id = ?', (cake_id,))
    cake = cursor.fetchone()
    if cake and cake[1] >= quantity:
        total_price = cake[0] * quantity
        new_stock = cake[1] - quantity
        cursor.execute('UPDATE cakes SET stock = ? WHERE id = ?', (new_stock, cake_id))
        cursor.execute('INSERT INTO sales (cake_id, quantity, total_price) VALUES (?, ?, ?)', (cake_id, quantity, total_price))
        conn.commit()
        conn.close()
        return True, total_price
    conn.close()
    return False, 0

def list_sales():
    conn = sqlite3.connect('cake_shop.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT sales.id, cakes.name, sales.quantity, sales.total_price, sales.sale_date
        FROM sales
        JOIN cakes ON sales.cake_id = cakes.id
    ''')
    sales = cursor.fetchall()
    conn.close()
    return sales
