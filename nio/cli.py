from nio.app import App
from nio.model.note import Note


class Cli(App):
    def __init__(self, con):
        super().__init__(con)

    def ls(self):
        for title in Note.get_titles(con=self.con):
            print(title)

    def print_help():
        pass

    def read(self, title: str):
        print(Note.loading(title, self.con))

    def search(self, keyword: str):
        print(Note.search(keyword, self.con))
