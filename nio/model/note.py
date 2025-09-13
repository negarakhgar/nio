from typing import Dict, List


class Note:
    def __init__(self, title: str, content: str, metadata: Dict[str, str]):
        assert isinstance(title, str)
        assert isinstance(content, str)

        assert isinstance(metadata, dict)
        for meta_key, meta_value in metadata.items():
            assert isinstance(meta_key, str)
            assert isinstance(meta_value, str)

        self.title = title
        self.content = content
        self.metadata = metadata

    def __repr__(self):
        return f"Note: {self.title}, {self.content}"

    def save(self, con):
        c = con.cursor()

        q = """
        INSERT INTO notes (title, content) VALUES (?, ?);
        """
        c.execute(q, (self.title, self.content))

        for meta_key, meta_value in self.metadata.items():
            q = """
            INSERT INTO metadata (title,meta_key,meta_value) VALUES (?,?,?);
            """
            c.execute(q, (self.title, meta_key, meta_value))

        con.commit()

    @staticmethod
    def loading(title: str, con):
        q = """
        
        select title, content, meta_key, meta_value 
        from notes 
        outer join metadata 
        on metadata.title=notes.title 
        where title = ?;
        """
        c = con.cursor()
        c.execute(q, [title])
        r = c.fetchall()
        if r is None or len(r) == 0:
            return None

        title, content, _, _ = r[0]
        metadata = {
            meta_key: meta_value for _title, _content, meta_key, meta_value in r
        }

        return Note(title, content, metadata)
