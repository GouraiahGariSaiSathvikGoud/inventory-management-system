import psycopg2
import psycopg2.extras

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "inventory_db",
    "user": "postgres",
    "password": "sathvik@2"  # replace with your actual password
}

def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            item_id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
