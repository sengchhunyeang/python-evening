# tuples unchangeable
myDay = ("monday", "tuesday", "wednesday", "thursday", "friday")
print(myDay)
print(myDay[1])

# set unchangeable but can remove or add new data

mySet = {"A","B"}
mySet.add("C")
print(mySet)

# Remove duplicates
numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers)  # {1, 2, 3, 4}
print(unique_numbers)

yourself = {"name":"Yeang","age":10 }
print(yourself["name"])