import psycopg2.extras
from database import get_connection

def add_item(name, category, quantity, price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, category, quantity, price) VALUES (%s, %s, %s, %s)",
        (name, category, quantity, price)
    )
    conn.commit()
    cursor.close()
    conn.close()

def get_all_items():
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def update_item_quantity(item_id, new_quantity):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE item_id = %s", (item_id,))
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        raise ValueError(f"Item ID {item_id} not found.")
    cursor.execute("UPDATE items SET quantity = %s WHERE item_id = %s", (new_quantity, item_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_item(item_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE item_id = %s", (item_id,))
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        raise ValueError(f"Item ID {item_id} not found.")
    cursor.execute("DELETE FROM items WHERE item_id = %s", (item_id,))
    conn.commit()
    cursor.close()
    conn.close()