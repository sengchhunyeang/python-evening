from colorama import Fore, Back, Style
END = "\033[0m"
GREEN = "\033[0;32m"
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"ID:{self.user_id}\nUserName:{self.name}\nUserEmail:{self.email}"


class UserMager:
    def __init__(self):
        self.users = []

    # create add_users function
    def add_users(self, user_id, name, email):
        user = User(user_id, name, email)
        self.users.append(user)
        print(Fore.RED + 'some red text')
        print(f"{GREEN}User added successfully.{END}")

    def view_user(self):
        for user in self.users:
            print(user)


def display_menu():
    print("=================System Manage User =================")
    print("1-Add User ")
    print("2-View User ")
    print("3-Update User")
    print("4-Delete User")
    print("5-Exit")
    print("=================System Manage User =================")


def input_option(option):
    if option == "1":
        user_id = input("Enter ID: ")
        name = input("Enter name :")
        email = input("Enter Email:")
        obj.add_users(user_id, name, email)
    elif option == "2":
        print("2-View User")
        obj.view_user()
    elif option == "3":
        print("3-Update User")
    elif option == "4":
        print("4-Delete User")
    elif option == "5":
        print("Program exiting...")
        exit(0)
    else:
        print("Something Wrong option ..!")


obj = UserMager()
while True:
    display_menu()
    opt = input("choose option do you want :")
    input_option(opt)
