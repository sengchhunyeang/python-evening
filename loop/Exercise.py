# 1. print number 1 to 10
# what is loops: repeat the same code

# for i in range(11): # start default 0 and Stop before 11
#     print(i)

# 2. print number 10 to 1
# for i in range(100, 0, -50):  # start form 10 decrement -1
#     print(i)

# increment +   0 1 2 3 4
# decrement -  10 9 8 7 ...0

# 3. number=[1,2,10] sum number value = 13
#
# numbers = [1, 2, 10]
# total = 0
# for i in numbers:
#     total += i # total = total + i
# print("Total list number : ",total)

# total = 0 + 1 + 2 +10 = 13

# practice

numbers = []
input_number = int(input("You want sum many number :"))
for i in range(input_number):
    num = int(input("number"))
    numbers.append(num)

    total = 0
    for num in numbers:
        total += num  # total = total + i
print("numbers : ", numbers)
print("Total : =", total)
