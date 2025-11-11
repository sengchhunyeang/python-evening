
print("1-Start Program")
print("2-Setting")
print("3-Exit")
choice = int(input("Enter your choice (1-3): "))
match choice:
    case 1:
        print("Start Program")
    case 2:
        print("Settings")
    case 3:
        print("Exit")
    case _:
        print("Invalid Choice")