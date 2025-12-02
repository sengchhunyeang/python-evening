# Banking System
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Transaction History
# 5. Exit

balance = 1000
history = []   # To store transactions

while True:
    print("======= Welcome to the Banking System =======")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    inputOption = input("Please select an option (1-5): ")

    match inputOption:
        case "1":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                history.append(f"Deposited {amount}")
                print(f"Your {amount} is deposited successfully")
            else:
                print("Invalid amount. Please enter a positive value.")

        case "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount >= 0 and amount <= balance:
                balance -= amount
                history.append(f"Withdrew {amount}")
                print(f"Your {amount} is withdrawn successfully")
            else:
                print(f"You can't withdraw {amount}")

        case "3":
            print(f"Your current balance is: {balance}")

        case "4":
            print("===== Transaction History =====")
            if not history:
                print("No transactions available.")
            else:
                for record in history:
                    print(record)

        case "5":
            print("Thank you for using the Banking System. Goodbye!")
            break
