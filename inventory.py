from database import get_connection

def add_item(name, category, quantity, price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, category, quantity, price) VALUES (?, ?, ?, ?)",
        (name, category, quantity, price)
    )
    conn.commit()
    conn.close()

def get_all_items():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_item_quantity(item_id, new_quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE item_id = ?", (item_id,))
    if not cursor.fetchone():
        conn.close()
        raise ValueError(f"Item ID {item_id} not found.")
    cursor.execute("UPDATE items SET quantity = ? WHERE item_id = ?", (new_quantity, item_id))
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE item_id = ?", (item_id,))
    if not cursor.fetchone():
        conn.close()
        raise ValueError(f"Item ID {item_id} not found.")
    cursor.execute("DELETE FROM items WHERE item_id = ?", (item_id,))
    conn.commit()
    conn.close()