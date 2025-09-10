# Simple Login & Register System in Terminal
# from ravid.module import getOption, homepageMenu
from module import *
users = {}  # Dictionary to store username: password


def register():
    print("\n--- Register ---")
    username = input("Enter new username: ")
    if username in users:
        print("Username already exists! Try again.")
    else:
        password = input("Enter new password: ")
        users[username] = password
        print("Registration successful!")


def login():
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("Login successful! Welcome,", username)
        print("Welcome Homepage")
        homepageMenu()
        var = input("choose option :")
        getOption(var)

    else:
        print("Invalid username or password.")


def main():
    while True:
        print("\n==== MENU ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again!")


