import sqlite3

def create_db():
    conn = sqlite3.connect('rms.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text, duration text, charges text, description text)")

    conn.commit()

    c.execute('''CREATE TABLE IF NOT EXISTS student(
        roll INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        gender TEXT,
        dob TEXT, contact TEXT, admission  TEXT,
        course TEXT,  state TEXT, city TEXT,
        pin TEXT, address TEXT
        )''')        
    
    conn.commit()            
    conn.close()

create_db()
