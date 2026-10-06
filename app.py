from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import time
from typing import Optional

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database and create history table
def init_database():
    conn = sqlite3.connect("calc_history.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS history
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  expression TEXT,
                  result TEXT,
                  create_time TEXT)''')
    conn.commit()
    conn.close()

init_database()

# 1. POST /api/calculate: receive expression and compute
@app.post("/api/calculate")
def calculate(data: dict):
    expression = data.get("expression")
    if not expression:
        return {"code": 500, "msg": "empty expression"}
    try:
        # Calculate on backend
        result = str(eval(expression))
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        # Insert record into database
        conn = sqlite3.connect("calc_history.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO history(expression, result, create_time) VALUES (?, ?, ?)",
            (expression, result, current_time)
        )
        conn.commit()
        conn.close()
        return {"code": 200, "data": {"result": result}}
    except Exception:
        return {"code": 500, "msg": "calculate error"}

# 2. GET /api/history: fetch all history records
@app.get("/api/history")
def get_history():
    conn = sqlite3.connect("calc_history.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, expression, result, create_time FROM history ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    record_list = []
    for row in rows:
        record_list.append({
            "id": row[0],
            "expression": row[1],
            "result": row[2],
            "time": row[3]
        })
    return {"code": 200, "data": record_list}

# 3. DELETE /api/history/{record_id}: delete single record
@app.delete("/api/history/{record_id}")
def delete_single_record(record_id: int):
    conn = sqlite3.connect("calc_history.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM history WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()
    return {"code": 200, "msg": "delete success"}

# 4. DELETE /api/history: clear all records
@app.delete("/api/history")
def delete_all_records():
    conn = sqlite3.connect("calc_history.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM history")
    conn.commit()
    conn.close()
    return {"code": 200, "msg": "clear all success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
