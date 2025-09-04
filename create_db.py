import sqlite3

def create_db():
    conn = sqlite3.connect('rms.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text, charges text, description text)")

    conn.commit()
    conn.close()
