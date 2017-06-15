import sqlite3

# test comment

class Database():

    def __init__(self, db):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn integer)")
        conn.commit()
        conn.close()

    def connect(self):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn integer)")
        conn.commit()
        conn.close()

    def insert(self, title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        conn.commit()
        conn.close()

    def view(self):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self, title = "", author = "", year = "", isbn = ""):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self, id):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def update(self, id, title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
        conn.commit()
        conn.close()

#insert("ASDFFF", "BERDA", 1234, 4213412412412)
#delete(3)
#update(1, "BASDF", "Prdez", 1932, 1293128392813)
#print(view())
#print(search(author = "BERDA"))
