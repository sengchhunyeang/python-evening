# create a funtion
def display_system():
    print("============= display system =============")

def print_name(name, age, gender):
    print(f"My name : {name}\tage:{age}\tgender :{gender}") # just show information 

def print_name(name,age):
    return f"name :{name} age: {age}"
# Called function

display_system()
name = input("Enter name :")
age = input("Enter age :")

# call method print_name(name,age,gender)


# storedata = print_name(name,age)
# print(storedata)

