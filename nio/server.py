from nio.model.note import Note
from nio.app import App


class Server(App):
    def __init__(self, con):
        super().__init__(con)

    def on_get_title(self, req, res, title: str):
        n = Note.loading(title=title, con=self.con)

        if n is None:
            res.status = 404
        else:
            res.media = {"title": n.title, "content": n.content}

    def on_delete_title(self, req, res, title: str):
        Note.delete(title, self.con)

    def on_post(self, req, res):
        obj = req.get_media()

        n = Note(title=obj["title"], content=obj["content"], metadata=obj["metadata"])
        n.save(con=self.con)

    def on_get_list(self, req, res):
        res.media = Note.get_titles(con=self.con)

    def on_post_search(self, req, res):
        obj = req.get_media()

        res.media = Note.search(keyword=obj["keyword"], con=self.con)
