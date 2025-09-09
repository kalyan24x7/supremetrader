from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
import os

app = FastAPI()

# Allow your frontend origin (Vercel) and local dev
origins = [
    "https://supremetrader.vercel.app",  # your deployed frontend
    "http://localhost:3000"              # local dev testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # for dev you could also use ["*"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI"}

@app.get("/items")
def get_items():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM items;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "name": r[1]} for r in rows]
