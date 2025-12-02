from colorama import Fore, Back, Style

balance = 100
transactions = []
while True:
    print("====Banking System====")
    print("1-Deposit")
    print("2-Withdraw")
    print("3-Check Balance")
    print("4-Transaction History")
    print("5-Exit")
    inputOption = int(input("Your Option:(1-5) :"))

    match inputOption:
        case 1:
            amount = float(input("Enter amount :"))
            if amount > 0:
                balance = balance + amount  # 0 100 + 50 + 45 + 48
                print(f"your {amount}$ Deposit Successful")
                transactions.append(f"deposit{amount} $")
            else:
                print(f"{Fore.RED}can not deposit {Fore.RESET}")
        case 2:
            amount = float(input("Enter your amount :"))
            if amount >= 0 and amount <= balance:
                balance = balance - amount
                print(f"your {amount}$ Withdraw Successful")
                transactions.append(f"withdraw{amount}$")
            else:
                print(f"{Fore.RED}Can not withdraw your {balance}${Fore.RESET}")
        case 3:
            print("Your Balance is :", balance, "$")
        case 4:
            print("===Transaction History===")
            if len(transactions) == 0:
                print("No Transactions")
            else:
                for history in transactions:
                    print(history)
        case 5:
            print(f"{Fore.BLUE}Banking Closed Thank you !{Fore.RESET}")
            print(exit())
