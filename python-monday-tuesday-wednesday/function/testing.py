# 1- function no param and no return
# 2- funtino no param and has return
# 3-funtion has param and no return
# 4-function has param and has return
# no param and no return
def message_alert():
    print("Python for you !")
    
# no param and has return
def message():
    return "python for you ! function Return "

messageAlert = message()
print(messageAlert)
# has param and no return
def message_name(name):
    print(f"my name :{name}")

# message_name("KeaRa")
def message_namereturn(name):
    return name
# practice
# create funtion :
# 1-function no param and no return
# 2-funtino no param and has return
# 3-funtion has param and no return
# 4-function has param and has return


def greeting(name,age):
    print(f"name :{name}\nage :{age}year")
    
greeting("Kirivong",45)
print("====================")
greeting(45,"kirivong")
greeting(age=45,name="Kirivong")