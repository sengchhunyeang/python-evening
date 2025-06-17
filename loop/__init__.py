
# for i in range(1,6):
#     print("*"*i)

#range(10) output : 0,1,2,3,4,5,6,7,8,9

# i = 0 < 9 = T => 0 love u
# i = 1 < 9 = T => 1 love u
#..........................
# i = 9 < 9 = F => Loop Terminate

# Homework using for loop
# 1. print number 1 to 10
# 2. print number 10 to 1
# 3. number=[1,2,10] sum number value = 13

# password = ""
# while password != "secret123":
#     password = input("Enter password: ")
# print("Access granted!")
# What if the user fails all 3 attempts?
for _ in range(3):
    password = input("Enter password: ")
    if password == "secret123":
        print("Access granted!")
        break
else:
    print("Too many attempts!")