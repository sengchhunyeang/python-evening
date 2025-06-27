# Function is a block of code that it runs when called
def my_Fun():
    print("Here running when called ")  # 1 block of Func


my_Fun()
# write once, using multiple times
# build-in-function
print()
# def sum(value1,value2): # user-df function
#     return value1+value2
value1 = 2
value2 = 3


# result = sum([value1,value2])
# print(result)

# Pratice Create one func that show information
# Print name
# print age
# print gender

def show_info():
    print("My name is <NAME>")
    print("My age is 20")
    print("My gender is male")


# How to declare function 4 way
# 1 function no parameter and no return
def nameFunction():
    print("function no parameter and no return ")


# 2 Function have parameter and no return
def functionWithParam(param):  # param like to variable
    print("Function have parameter and no return", param)


# 3 Function have return but no parameter
def funcNoReturn():
    return "This is Function have return but no parameter"


# 4 Function have return and have parameter
def funcWithParamReturn(param):
    return param


def add():
    return 200  # money 200 riel
soa_leang = add()
print(soa_leang)
soa_leang+=100
print(soa_leang)

# create function have parameter no return
print("="*40)
def show_information(name,age,gender): # parameter
    print("Here my Information")
    print("My name is :",name)
    print("My age is :,",age)
    print("My gender is :,",gender)


show_information("Chhunyeang",25,"Male")
print("="*40)
show_information("Viseth",26,"Male") #Argument
