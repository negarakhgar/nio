from nio.app import App
from nio.model.note import Note


class Cli(App):
    def __init__(self, con):
        super().__init__(con)

    def ls(self):
        for title in Note.get_titles(con=self.con):
            print(title)

    @staticmethod
    def print_help():
        print("""nio-cli
author :negar akhgar 
cli application for taking notes 

commands:
ls
        list of the save notes 
add <title> <content> [<metadata_key> <metadata_value>]+
        add notes 
read <title>
        read a saved note
search <keyword>
        search by keyword                              
        """)

    def read(self, title: str):
        print(Note.loading(title, self.con))

    def search(self, keyword: str):
        print(Note.search(keyword, self.con))

    def add(self, title, content, metadata):
        n = Note(title, content, metadata)
        n.save(self.con)

    def delete(self, title):
        Note.delete(title, self.con)
