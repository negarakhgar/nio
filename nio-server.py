from wsgiref import simple_server
from nio.server import Server
import sqlite3
import falcon

con = sqlite3.connect("nio.db")

with open("migrations/setup.sql") as m:
    con.executescript(m.read())


# n = Note(title="email", content="negar", metadata=dict())
# n.save(con)

# n = Note.loading(title="email", con=con)
# print(n)

app = falcon.App()
s = Server(con)
app.add_route("/note", s)
app.add_route("/note/{title}", s, suffix="title")
app.add_route("/notes", s, suffix="list")
app.add_route("/notes/search", s, suffix="search")

httpd = simple_server.make_server("127.0.0.1", 8000, app)
httpd.serve_forever()

con.close()
