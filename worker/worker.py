import psycopg2
import os
import time
import random

DATABASE_URL = os.getenv("DATABASE_URL")
items = ["Apple", "Banana", "Orange", "Grapes"]

def get_connection():
    return psycopg2.connect(DATABASE_URL)

while True:
    conn = get_connection()
    cur = conn.cursor()
    item = random.choice(items)
    cur.execute("INSERT INTO items (name) VALUES (%s);", (item,))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted {item}")
    time.sleep(30)