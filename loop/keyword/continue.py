# continue and break
# print("Continue")
# for i in range(1, 10): # 1-9 or 10
#     if i == 5:
#         continue # skip
#     print(i)
# print("="*40)
# print("Break")
# for i in range(1, 10): # 1-9 or 10
#     if i == 5:
#         break
#     print(i)

# while True :
#     user_input = int(input("input number 1-10 :" ))
#     if user_input == 0 :
#         print("code Exite")
#         break

# for i in range(1, 11,): # 1-9 or 10
#     if i % 2 == 0:
#             print(i)

listNumber = [1,2,3,4,5,6,7,8,9,10] # I don't want to show number 6
for i in listNumber:
    if i != 5:
        print(i ,end="-")