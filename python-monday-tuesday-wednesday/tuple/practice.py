# Pratice Method
# creat new tuple 1 = (5,6,6,7,8)
# 1 - print tuple show on console
# 2 - Using index function and count
# 3 - Convert to list
# 4 - Change value all in list that converted

numberTuple = (5, 6, 6, 6, 7, 8)
print("print tuple show on console:", numberTuple)
print("Show index number 8 :", numberTuple.index(8))
print("Show Duplicated Count :", numberTuple.count(6))

conTupleToList = list(numberTuple)
print("Convert to list:", conTupleToList)
conTupleToList[0:6] = [1, 2, 3, 4, 5, 6, 7]  # Start =0 end 6
conTupleToList[0] = 1
conTupleToList[1] = 2
conTupleToList[2] = 3
conTupleToList[3] = 4
conTupleToList[4] = 5
conTupleToList[5] = 6
print("List Changed :", conTupleToList)
numberTuple = (5, "Apple", 6, 6, 7, 8)
log = numberTuple[1]
showIndex = numberTuple.index(8)
print("SHow Index number 8 :", showIndex)
print(log)
logIndex5 = numberTuple[5]
print("logIndex5", type(logIndex5))
print(type(log))
