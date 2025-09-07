from typing import Dict, List


class Note:
    def __init__(self, title: str, content: str, metadata: Dict[str, List[str]]):
        self.title = title
        self.content = content
        self.metadata = metadata

    def __repr__(self):
        return f"Note: {self.title}, {self.content}"

    def save(self, con):
        q = """
        INSERT INTO notes (title, content) VALUES (?, ?);
        """
        c = con.cursor()
        c.execute(q, (self.title, self.content))
        con.commit()

    @staticmethod
    def loading(title: str, con):
        q = """
        select title ,content from notes where title =? ;
        """
        c = con.cursor()
        c.execute(q, [title])
        r = c.fetchone()
        if r is None or len(r) == 0:
            return None

        title, content = r
        return Note(title, content, metadata=None)
