class classroom:
    def __init__(self):
        self.children = list()
        self.tags = {}


class person:
    def __init__(self, name, family):
        self.name = name
        self.family = family
        self.my_classroom = classroom()
        self.title = "Mr"


teacher_a = person(name="Gigia", family="Bianchi")

print(teacher_a.name)
print(teacher_a.my_classroom.children)


class student(person):
    def __init__(self, name, family, age):
        super().__init__(name, family)
        self.age = age


student_a = student("Negar", "Akhgar", 28)

print(student_a.my_classroom)
print(student_a.age)
