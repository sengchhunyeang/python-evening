import time as t
import json
import os
data = {}
def load_data():
    if os.path.exists('bank_data.json'):
        with open('bank_data.json') as f:
            return json.load(f)
    else:
        return {}  # no accounts yet

def save_data(data):
    with open('bank_data.json', 'w') as f:
        json.dump(data, f, indent=4)
def ask():
    question = input(
        "===== BANKING =====\n"
        "1. Check Balance\n"
        "2. Deposit Funds\n"
        "3. Withdraw Funds\n"
        "4. Transaction History\n"
        "5. Transfer Money\n"
        "6. Exit\n"
        "Select an option (1-6):\n"
    )
    return question
def wait(seconds):
    t.sleep(seconds)
def check_balance(balance, balance_riel):
    print(f"Your current balance is: ${balance:.2f} / {balance_riel:.0f}៛")
def deposit_funds(balance, balance_riel, history):
    currency = input("Currency to deposit (USD/$ or Riel/៛)? ").lower()
    try:
        amount = float(input("Enter amount: "))
    except:
        print("Invalid amount.")
        return balance, balance_riel

    if amount <= 0:
        print("Invalid deposit amount.")
        return balance, balance_riel

    if currency in ["usd", "$"]:
        balance += amount
        history.append(f"Deposited: ${amount:.2f}")
        print(f"${amount:.2f} deposited successfully.")
    elif currency in ["riel", "៛"]:
        balance_riel += amount
        history.append(f"Deposited: {amount:.0f}៛")
        print(f"{amount:.0f}៛ deposited successfully.")
    else:
        print("Invalid currency.")

    return balance, balance_riel

def withdraw_funds(balance, balance_riel, history):
    currency = input("Currency to withdraw (USD/$ or Riel/៛)? ").lower()
    try:
        amount = float(input("Enter amount: "))
    except:
        print("Invalid amount.")
        return balance, balance_riel

    if amount <= 0:
        print("Invalid withdrawal amount.")
        return balance, balance_riel

    if currency in ["usd", "$"]:
        if amount > balance:
            print("Insufficient USD funds.")
        else:
            balance -= amount
            history.append(f"Withdrew: ${amount:.2f}")
            print(f"${amount:.2f} withdrawn successfully.")
    elif currency in ["riel", "៛"]:
        if amount > balance_riel:
            print("Insufficient Riel funds.")
        else:
            balance_riel -= amount
            history.append(f"Withdrew: {amount:.0f}៛")
            print(f"{amount:.0f}៛ withdrawn successfully.")
    else:
        print("Invalid currency.")

    return balance, balance_riel

def transaction_history(history):
    if history:
        print("Transaction History:")
        for record in history:
            print(record)
    else:
        print("No transactions yet.")

def transfer_money(username, accounts):
    target = input("Enter username to transfer to: ")

    if target not in accounts:
        print("That user does not exist.")
        return

    try:
        amount = float(input("Enter amount to transfer: $"))
    except:
        print("Invalid input.")
        return

    if amount <= 0:
        print("Invalid transfer amount.")
        return

    if accounts[username]["balance"] < amount:
        print("Insufficient funds.")
        return
    accounts[username]["balance"] -= amount
    accounts[target]["balance"] += amount

    accounts[username]["history"].append(f"Transferred ${amount:.2f} to {target}")
    accounts[target]["history"].append(f"Received ${amount:.2f} from {username}")

    save_data(accounts)
    print(f"Successfully transferred ${amount:.2f} to {target}.")

def main_log(username, accounts):
    balance = accounts[username]["balance"]
    balance_riel = accounts[username].get("balance_riel", 0.0)
    history = accounts[username]["history"]

    while True:
        choice = ask()
        if choice == "1":
            check_balance(balance, balance_riel)
            wait(1)
        elif choice == "2":
            balance, balance_riel = deposit_funds(balance, balance_riel, history)
        elif choice == "3":
            balance, balance_riel = withdraw_funds(balance, balance_riel, history)
        elif choice == "4":
            transaction_history(history)
        elif choice == "5":
            transfer_money(username, accounts)
        elif choice == "6":
            print("Saving and exiting. Goodbye!")
            break
        else:
            print("Invalid option.")

        accounts[username]["balance"] = balance
        accounts[username]["balance_riel"] = balance_riel
        accounts[username]["history"] = history
        save_data(accounts)
        wait(1)
def main():
    accounts = load_data()

    while True:
        option = input(
            "===== BANKING =====\n"
            "1. Sign up (Create Account)\n"
            "2. Login\n"
            "3. Exit\n"
        )

        if option == "1":
            username = input("Create username: ")

            if username in accounts:
                print("Account already exists!")
                continue
            else:
                try:
                    #delete int() to allow any password
                    password = str(int(input("Create password: ")))
                except ValueError:
                    print("Invalid! Password must be a number.")

            accounts[username] = {
                "password": password,
                "balance":80,
                "balance_riel": 0.0,
                "history": []
            }

            save_data(accounts)
            print("Account created successfully.")

        elif option == "2":
            username = input("Username: ")

            if username not in accounts:
                print("Account does not exist.")
                continue

            password = input("Password: ")

            if password != accounts[username]["password"]:
                print("Incorrect password.")
                continue

            print("Login successful!")
            main_log(username, accounts)

        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
#delete int() to allow any password
main()