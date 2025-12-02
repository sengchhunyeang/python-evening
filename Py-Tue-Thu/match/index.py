# match ??

number = 10

match number:
    case 0:
        print("number is Zero")
    case 1:
        print("number is One ")
    case 2:
        print("number is Two")
    case _:  # else
        print("number have not matched ")


# condition ??
password = "admin123"
if password == "admin123":
    print("Login Successful")

# match ??
day = "Monday"
match day:
    case "Monday":
        print("Today is Monday")
    case "Tuesday":
        print("Today is Tuesday")
