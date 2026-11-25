import sqlite3

connection = sqlite3.connect("shop.db")

cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    total REAL NOT NULL CHECK (total >= 0),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL CHECK (price >= 0)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
""")

customer_data = [
    ("Alan", "London"),
    ("Baccus", "Berlin"),
    ("Cliff", "Massachusetts")
]

product_data = [
    ("Monitor", 256),
    ("Keyboard", 128)
]

cursor.execute(
    "INSERT INTO customers (name, city) VALUES (?, ?)", customer_data
)

connection.commit()
connection.close()