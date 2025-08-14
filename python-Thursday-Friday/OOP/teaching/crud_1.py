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
        # print(Fore.RED + 'some red text')
        print(f"{GREEN}User added successfully.{END}")

    def view_user(self):
        for user in self.users:
            print(user)

    def update_user(self, user_id, new_name, new_email):
        for user in self.users:
            if user.user_id == user_id:
                user.name = new_name
                user.email = new_email
                print(f"{GREEN}User updated successfully.{END}")
                return
        print("not found")
    def delete_user(self,user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                print(f"{GREEN}User deleted successfully.{END}")
                return
        print("not found")


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
        obj.update_user(
            user_id=(input("Enter ID: ")),
            new_name=input("Enter new name: "),
            new_email=input("Enter new email: "))
    elif option == "4":
        print("4-Delete User")
        obj.delete_user(user_id=(input("Enter ID: ")))
    elif option == "5":
        print("Program exiting...")
        exit(0)
    else:
        print("Something Wrong option ..!")


obj = UserMager()
obj.add_users("1","Kirivong","kivirivong@gmail.com")
obj.add_users("2","chan dara","dara@gmail.com")
while True:
    display_menu()
    opt = input("choose option do you want :")
    input_option(opt)
