from idlelib.colorizer import prog_group_name_to_tag

myNumber = [8, 4, 5, 6, 3]


def minimumList(param):
    return min(param)


def maximumList(param):
    return max(param)


def printEvenList(param):
    return [variable for variable in param if variable % 2 == 0]


def printOddList(param):
    return [variable for variable in param if variable % 2 != 0]

def sumList(param):
    return sum(param)

print("list number that min :",minimumList(myNumber))
print("list number that max :",maximumList(myNumber))
print("List even number :",printEvenList(myNumber))
print("List odd number ",printOddList(myNumber))

print(sumList(myNumber))