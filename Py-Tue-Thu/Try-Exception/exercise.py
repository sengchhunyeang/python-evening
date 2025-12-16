
# practice using try-exception
while True:
    try:
        var = int(input("age :"))
        print("you are :",var)
    except ValueError:
        print(" Incorrect Please input again ")

# print("Here value ",var)