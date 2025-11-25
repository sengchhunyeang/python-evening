import json
import os
import time
from datetime import datetime

DATA_FILE = "bank_data.json"

# ----------------------- DATA HANDLING -----------------------
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"accounts": {}}

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ----------------------- ACCOUNT CREATION -----------------------
def create_account(data):
    print("\n===== CREATE NEW ACCOUNT =====")
    username = input("Create username: ")

    if username in data["accounts"]:
        print("Username already exists!")
        return

    pin = input("Create 4-digit PIN: ")
    if len(pin) != 4 or not pin.isdigit():
        print("PIN must be 4 digits!")
        return

    data["accounts"][username] = {
        "pin": pin,
        "balance_usd": 0,
        "balance_riel": 0,
        "transactions": []
    }

    save_data(data)
    print("Account created successfully!")


# ----------------------- LOGIN SYSTEM -----------------------
def login(data):
    print("\n===== LOGIN =====")
    username = input("Username: ")

    if username not in data["accounts"]:
        print("Account not found!")
        return None

    pin = input("PIN: ")

    if pin == data["accounts"][username]["pin"]:
        print("Login successful!")
        return username
    else:
        print("Wrong PIN!")
        return None


# ----------------------- TRANSACTION ID -----------------------
def generate_tid():
    return f"T{int(time.time())}"


# ----------------------- BANKING FUNCTIONS -----------------------
def deposit(user, data):
    print("\n===== DEPOSIT MONEY =====")
    print("1. USD ($)")
    print("2. Riel (៛)")
    c = input("Choose currency: ")

    amount = float(input("Amount: "))

    if amount <= 0:
        print("Invalid amount!")
        return

    tid = generate_tid()

    if c == "1":
        data["accounts"][user]["balance_usd"] += amount
        data["accounts"][user]["transactions"].append(
            {"id": tid, "type": "Deposit", "currency": "USD", "amount": amount, "time": str(datetime.now())}
        )
    elif c == "2":
        data["accounts"][user]["balance_riel"] += amount
        data["accounts"][user]["transactions"].append(
            {"id": tid, "type": "Deposit", "currency": "KHR", "amount": amount, "time": str(datetime.now())}
        )
    else:
        print("Invalid currency!")
        return

    save_data(data)
    print(f"Deposit successful! (Transaction ID: {tid})")


def withdraw(user, data):
    print("\n===== WITHDRAW MONEY =====")
    print("1. USD ($)")
    print("2. Riel (៛)")
    c = input("Choose currency: ")

    amount = float(input("Amount: "))

    if amount <= 0:
        print("Invalid amount!")
        return

    tid = generate_tid()

    acc = data["accounts"][user]

    if c == "1":
        if amount <= acc["balance_usd"]:
            acc["balance_usd"] -= amount
            acc["transactions"].append(
                {"id": tid, "type": "Withdraw", "currency": "USD", "amount": amount, "time": str(datetime.now())}
            )
        else:
            print("Not enough USD!")
            return

    elif c == "2":
        if amount <= acc["balance_riel"]:
            acc["balance_riel"] -= amount
            acc["transactions"].append(
                {"id": tid, "type": "Withdraw", "currency": "KHR", "amount": amount, "time": str(datetime.now())}
            )
        else:
            print("Not enough Riel!")
            return

    else:
        print("Invalid currency!")
        return

    save_data(data)
    print(f"Withdraw successful! (Transaction ID: {tid})")


def view_balance(user, data):
    acc = data["accounts"][user]
    print("\n===== BALANCE =====")
    print(f"USD: ${acc['balance_usd']}")
    print(f"Riel: {acc['balance_riel']}៛")


def view_history(user, data):
    print("\n===== TRANSACTION HISTORY =====")
    acc = data["accounts"][user]["transactions"]

    if not acc:
        print("No transactions yet.")
        return

    for t in acc:
        print(f"[{t['id']}] {t['type']} {t['amount']} {t['currency']} - {t['time']}")


# ----------------------- MAIN MENU -----------------------
def user_menu(username, data):
    while True:
        print("\n===== BANK MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Logout")

        choice = input("Choose: ")

        if choice == "1":
            deposit(username, data)
        elif choice == "2":
            withdraw(username, data)
        elif choice == "3":
            view_balance(username, data)
        elif choice == "4":
            view_history(username, data)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")


# ----------------------- MAIN SYSTEM LOOP -----------------------
def main():
    data = load_data()

    while True:
        print("\n===== BANKING SYSTEM =====")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            user = login(data)
            if user:
                user_menu(user, data)

        elif choice == "2":
            create_account(data)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option!")
main()
