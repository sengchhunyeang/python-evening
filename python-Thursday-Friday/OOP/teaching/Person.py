# 1 create class Person
# 2 state name gender position

class Person:
    
    def __init__(self,name,gender,postion):
        self.name = name 
        self.gender= gender
        self.position = postion
    def get_infor(seft):
        print("name:",seft.name)
        print("Gender:",seft.gender)
        print("Position:",seft.position)

person1 = Person(name="Hook",gender="male",postion="IT")
person2 = Person(name="Ury",gender="Female",postion="Accounting")
# print(person1.name,person1.position)
# print(person2.name,person2.position)
print(person1.get_infor())


