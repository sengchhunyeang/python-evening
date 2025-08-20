compare_value = lambda x, y: "x is smaller than y" if x < y else ("x is greater than y" if x > y else "x is equal to y")

# value_x = input("Please enter the value x: ")
# value_y = input("Please enter the value y: ")
#
# result = compare_value(value_x, value_y)
# print(result)
compare_number = lambda a,b:  min(a,b)  if a < b else max(a,b)

print(compare_number(4,5))

