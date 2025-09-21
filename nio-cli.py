import sqlite3
import sys

from nio.cli import Cli
# for creat application

con = sqlite3.connect("nio.db")

with open("migrations/setup.sql") as m:
    con.executescript(m.read())

cli = Cli(con)

match len(sys.argv):
    case 0:
        print("impossible")
    case 1:
        cli.print_help()
    case _:
        sys.argv.pop(0)

        # print("Command:", sys.argv[1])
        match sys.argv.pop(0):
            case "add":
                title = sys.argv.pop(0)
                content = sys.argv.pop(0)
                metadata = {}
                while len(sys.argv) > 0:
                    key = sys.argv.pop(0)
                    value = sys.argv.pop(0)
                    metadata[key] = value
                cli.add(title, content, metadata)
            case "read":
                title = sys.argv.pop(0)
                cli.read(title)
            case "search":
                keyword = sys.argv.pop(0)
                cli.search(keyword)
            case "ls":
                cli.ls()
            case "delete":
                title = sys.argv.pop(0)
                cli.delete(title)
