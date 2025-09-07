from nio.model.note import Note


class Server:
    def __init__(self, con):
        self.con = con

    def on_get_title(self, req, res, title: str):
        n = Note.loading(title=title, con=self.con)

        if n is None:
            res.status = 404
        else:
            res.media = {"title": n.title, "content": n.content}

    def on_post(self, req, res):
        obj = req.get_media()

        n = Note(title=obj["title"], content=obj["content"], metadata={})
        n.save(con=self.con)

    def on_get_list(self, req, res):
        q = """
            select title from notes ;
            """

        c = self.con.cursor()
        c.execute(q, [])
        r = c.fetchall()

        if r is None:
            r = []

        res.media = [j for i in r for j in i]
