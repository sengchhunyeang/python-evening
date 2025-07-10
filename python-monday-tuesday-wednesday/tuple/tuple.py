myTuple = ("Apple", "Oragne", "Banana")  # Index = 0....last index 120 (3= 0.1.2)
print(myTuple)
# Access by index
print(myTuple[0])

conTupleTolist = list(myTuple)
print("Convert to list :", conTupleTolist)

# Day of weeks

# print(dayOfweek)
# # Tuple Unchangeble
# print("Index of Sunday :", dayOfweek.index("Sun"))
# print("Duplicated day :", dayOfweek.count("Wed"))


# Pratice Method
# creat new tuple 1 = (5,6,6,7,8)
# 1 - print tuple show on console
# 2 - Using index function and count
# 3 - Convert to list
# 4 - Change value all in list that converted

dayOfweek = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
# How index of dayOfWeek
# Example:
# result : Mon = index:0
# result : Tue = index:1
# ........................
# result : Sun = index:5
logIndexOfMon = dayOfweek.index("Mon")
print("Index of Mon :",logIndexOfMon)