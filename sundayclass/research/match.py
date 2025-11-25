print("1.Deposit")
print("2.Withdraw")
print("3.check balance")
print("4.Transition History")
print("5.Exit")
option = int(input("chose option (1-5): "))
deposit = 0
match option:
    case 1:
        print("Deposit")
    case 2:
        print("Withdraw")
    case 3:
        print("Check balance")
    case 4:
        print("Transition History")
    case 5:
        print("Exit")
