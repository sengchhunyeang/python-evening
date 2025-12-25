# create a class student
class Student:
    # Attribute
    # __init__ defaul construtor
    def __init__(self, id, name, class_room, mark, gender):
        # self.id : Attribute
        # id : Parameter
        self.id = id
        self.name = name
        self.clas_room = class_room
        self.mark = mark
        self.gender = gender

    # function for get data from class
    def __str__(self):
        return f"id:{self.id}\nname:{self.name}\nclassroom:{self.clas_room}\ngender:{self.gender}"
