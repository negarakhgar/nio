from typing import Dict, List
import sqlite3


class Note:
    def __init__(self, title: str, content: str, metadata: Dict[str, List[str]]):
        self.title = title
        self.content = content
        self.metadata = metadata

    def save(self, con):
        q = """
        INSERT INTO notes (title, content) VALUES (?, ?);
        """
        c = con.cursor()
        c.execute(q, (self.title, self.content))
        con.commit()
