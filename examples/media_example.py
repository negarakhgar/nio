from abc import ABC


class Media(ABC):
    def __init__(self, title: str):
        self.title = title
        # self.my_function = lambda s: print(s)

    def id(self):
        return self.title.replace(" ", "-")

    # def my_function(s):
    # print(s)


m = Media("example")
# m.my_function("afafasfafaasfasfasasafa")


class Note(Media):
    def __init__(self, title, content):
        super().__init__(title)
        self.content = content


obj1 = Note("red flower", 100)
print(obj1.content)
print(obj1.id())
