import json
import os

# JSON file to store user accounts
Data_File = "Banking account.json"

# Load JSON database

def Load_data():
    if not os.path.exists(Data_File):
        with open(Data_File, "w") as f:
            json.dump({}, f)
    with open(Data_File, "r") as f:
        return json.load(f)

# Save JSON database

def save_db(db):
    with open(Data_File, "w") as f:
        json.dump(db, f, indent=4)

# Create new account

def create_account():
    data = Load_data()

    username = input("Enter username: ")
    if username in data:
        print("Username already exists! Try another one.")
        return

    password = input("Enter password: ")

    data[username] = {
        "password": password,
        "balance": 0
    }

    save_db(data)
    print("Account created successfully!\n")

# Login

def login():
    db = Load_data()

    username = input("Username: ")
    password = input("Password: ")

    if username in db and db[username]["password"] == password:
        print("Login successful!\n")
        user_menu(username)
    else:
        print("Invalid username or password!\n")

# User menu after login

def user_menu(username):
    while True:
        print("==== USER MENU ====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")

        choice = input("Enter choice: ")
        data = Load_data()

        if choice == "1":
            print(f"Your balance: {data[username]['balance']}\n")

        elif choice == "2":
            amount = int(input("Deposit amount: "))
            data[username]["balance"] += amount
            save_db(data)
            print("Deposit successful!\n")

        elif choice == "3":
            amount = int(input("Withdraw amount: "))
            if amount <= data[username]["balance"]:
                data[username]["balance"] -= amount
                save_db(data)
                print("Withdraw successful!\n")
            else:
                print("Not enough balance!\n")

        elif choice == "4":
            print("Logged out!\n")
            break

        else:
            print("Invalid option!\n")

# Main program

def main():
    while True:
        print("==== SIMPLE BANK SYSTEM ====")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option!\n")

main()