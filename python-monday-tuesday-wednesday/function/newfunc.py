# function 2 type
# build-in function

# user define function
def greeting_message():
    print("Welcome to ICT again !")


def message_smart(name):  # keyword def name func: message_smart() body: print(..........)
    print(f"smart {name} !")


def message_infor(name, age):
    print(f"name :{name},age:{age}")


def circle():
    return 3.14


# call

message_smart("smile")
message_smart("Cry")
message_smart(".....")
message_infor("Nana", 45)
message_infor(age=45, name="nana")

numOfcircle = circle()
print(numOfcircle)