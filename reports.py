from database import get_connection

def total_inventory_value():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(quantity * price) AS total_value FROM items")
    result = cursor.fetchone()
    conn.close()
    return result["total_value"] or 0

def low_stock_report(threshold=5):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE quantity <= ?", (threshold,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def category_summary():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT category, COUNT(*) as item_count, SUM(quantity) as total_qty, SUM(quantity * price) as value
        FROM items GROUP BY category
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows