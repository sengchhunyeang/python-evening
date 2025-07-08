print("print list")

list = [1, 2, 5, 6, 2, 3]
list.sort()
print(list)

otherList = list.copy()
print("Other list :", otherList)

clearList = otherList.clear()
print("Clear List :", clearList)

count = list.count(5)
print("print count :",count)