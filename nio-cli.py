import os
import sqlite3
import sys

from nio.cli import Cli

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
        # print("Command:", sys.argv[1])
        match sys.argv[1]:
            case "add":
                pass
            case "load":
                pass
            case "ls":
                for title in cli.ls():
                    print(title)
