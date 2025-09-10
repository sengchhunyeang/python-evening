
# How to declare list in Python 
myList = ["English","Korean","Khmer"] # 3item = 3index= 
# kimkheng index 1 
# puon index 0 
# item = 3 , 1,2,3
# index = 3 , 0,1,2

# print(type(myList))
# print("My data :",myList)
# print("My Index :",myList[1]) # korean 



multi = int(input("Input multi number: "))
number = int(input("Input number: "))

for i in range(1, number + 1):   # start from 1 up to number
    result = multi * i
    print(f"{multi} x {i} = {result}")

    
# 5 * 1 = 5 
# 5 * 2 = 10