from UserManager import *
def show():
    print("--------------System Manage User--------------- ")
    print("1 - Add User")
    print("2 - View User")
    print("3 - Update User")
    print("4 - Delete User")
    print("5 - Exit")
    print("-----------------------------------------------")

obj = UserManager()
def input_option(option, obj):
    if option == "1":
        user_id = input("Enter ID: ")
        user_name = input("Enter Name: ")
        user_email = input("Enter Email: ")
        obj.add_user(user_id, user_name, user_email)

    elif option == "2":
        obj.view_user()

    elif option == "3":
        user_id = input("Enter ID to update: ")
        new_name = input("Enter new name (leave blank to keep same:")
        new_email = input("Enter new email (leave blank to keep same: ")
        obj.update_user(user_id, new_name if new_name else None, new_email if new_email else None)

    elif option == "4":
        user_id = input("Enter ID to delete: ")
        obj.delete_user(user_id)

    elif option == "5":
        print("Program exiting...")
        exit(0)
    else:
        print("Invalid option, please try again.")

def say_hello():
    print("Hello World!")
