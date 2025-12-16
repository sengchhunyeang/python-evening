from Person import *

name = input("Input name :")
age = int(input("Input age :"))
gender = input("Input gender :")
company = input("Input company :")
job = input("Input job :")

# object instance from class Person
# creation object
Object = Person(name, age, gender, company, job)
Object.getAllData()
