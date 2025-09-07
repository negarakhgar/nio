from nio.model.note import Note


class Server:
    def __init__(self, con):
        self.con = con

    def on_get(self, req, res, title: str):
        n = Note.loading(title=title, con=self.con)

        if n is None:
            res.status = 404
        else:
            res.media = {"title": n.title, "content": n.content}
