from nio.app import App
from nio.model.note import Note


class Cli(App):
    def __init__(self, con):
        super().__init__(con)

    def ls(self):
        return Note.get_titles(con=self.con)

    def print_help():
        pass
