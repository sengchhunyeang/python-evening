from colorama import Fore as Color


class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"ID:{Color.BLUE}{self.user_id}{Color.RESET}\nUserName:{self.name}\nUserEmail:{self.email}"


class UserMager:
    def __init__(self):
        self.users = []

    # create add_users function
    def add_users(self, user_id, name, email):
        user = User(user_id, name, email)
        self.users.append(user)
        # print(Fore.RED + 'some red text')
        print(f"{Color.GREEN}User added successfully.{Color.RESET}")

    def view_user(self):
        for user in self.users:
            print(user)

    def update_users(self, find_user_id, new_name, new_email):
        for user in self.users:
            # check id , Find id
            if user.user_id == find_user_id:
                user.name = new_name
                user.email = new_email
                print(f"{Color.GREEN}Update successfully{Color.RESET}")
                return
        print(f"{Color.YELLOW}ID not found {Color.RESET}")

    # delete
    def delete_user(self, delete_user_id):
        for user in self.users:
            if user.user_id == delete_user_id:
                self.users.remove(user)
                print(f"{Color.GREEN}Delete user successfully {Color.RESET}")
            return
        print(f"{Color.YELLOW}users not found {Color.RESET}")


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
        obj.update_users(
            find_user_id=input("update id :"),
            new_name=input("update name :"),
            new_email=input("update email :")
        )
    elif option == "4":
        print("4-Delete User")
        obj.delete_user(
            delete_user_id=input("user id :")
        )
    elif option == "5":
        print("Program exiting...")
        exit(0)
    else:
        print("Something Wrong option ..!")


obj = UserMager()
obj.add_users("1", "Kirivong", "kivirivong@gmail.com")
obj.add_users("2", "chan dara", "dara@gmail.com")
while True:
    display_menu()
    opt = input("choose option do you want :")
    input_option(opt)
