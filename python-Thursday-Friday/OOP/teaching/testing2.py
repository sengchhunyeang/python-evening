# a class having :
# Attribute ?? Person id name age position 
# method
# class Person:
#     def __init__(self,id,name,age,position):
#         self.id = id 
#         self.name = name
#         self.age = age
#         self.position = position
   
#     def getDataPerson(self):
#         print(" id :",self.id)
#         print(" name :",self.name)
#         print(" age :",self.age)
#         print(" position ",self.position)

# # i want to instance data in class
# panharith = Person("12233","panharith","9","student")
# viseth = Person("123","Viseth","23","Python learner")
# chhunyeang = Person("1234","Chhunyeang","30","Instuctor ")
# # panharith.getDataPerson()

# # viseth.getDataPerson()

# chhunyeang.getDataPerson()
# class Persons:
#     def __init__(self,id,age,name):
#          self.id = id
#          self.age = age
#          self.name = name
#
#     def get_info(self): # just print or show data for user (Method)
#         print(" person's id digit is:", self.id)
#         print(" person's age is:", self.age)
#         print(" person's name is:", self.name)
# chhunyeang =Persons("89","78","Yeang") # insert data
# chhunyeang.get_info()

from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')