def bankingRunning():
    balance = 0  # starting money
    transactions = []  # store history

    while True:
        print("\n===== SIMPLE BANKING SYSTEM =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Choose option (1-5): ")

        # Deposit
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                transactions.append(f"Deposited: ${amount}")
                print("Deposit successful!")
            else:
                print("Invalid amount!")

        # Withdraw
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance and amount > 0:
                balance -= amount
                transactions.append(f"Withdrawn: ${amount}")
                print("Withdraw successful!")
            else:
                print("Not enough balance or invalid amount!")

        # Check balance
        elif choice == "3":
            print(f"Current Balance: ${balance}")

        # Transaction History
        elif choice == "4":
            print("\n--- Transaction History ---")
            if len(transactions) == 0:
                print("No transactions yet.")
            else:
                for t in transactions:
                    print(t)

        # Exit
        elif choice == "5":
            print("Thank you for using our bank system!")
            break

        # Invalid Input
        else:
            print("Invalid option, please try again.")
