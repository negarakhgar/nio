from nio.model.note import Note
import sqlite3

con = sqlite3.connect("nio.db")
with open("migrations/setup.sql") as m:
    con.executescript(m.read())


n = Note(title="email", content="negar", metadata=dict())
n.save(con)


con.close()
