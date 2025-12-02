timeInput = 3
increment = 1

while increment <= timeInput:
    password = input("Enter Password :")
    if password == "admin123":
        print("It correct password")
        break  # break terminate
    elif increment == 3:
        print("You enter password 3 time !")
        print(exit())
    else:
        print(f"Increament : {increment}")
        increment += 1  # 1+1+1 = 3
        print("password wrong")

# chhunyeangseng
# 12345@$%chsg
