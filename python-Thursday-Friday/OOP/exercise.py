# what is a class ? class blueprint for create an object 
# what is object ? 
# How to declare class ?
# class Person :
#     # Attribute 
#     name = "Viseth"
#     age = "23"
#     position = "IT"
# # How to instance object from class 
  
# obj= Person()
# viseth = obj.name
# visethAge = obj.age
# print("Name:",viseth)
# print("age :",visethAge)
    

from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

print(Fore.GREEN + "✅ Success message")
print(Fore.RED + "❌ Error message")
print(Fore.YELLOW + "⚠️ Warning")
print(Style.BRIGHT + "Bold Text")
