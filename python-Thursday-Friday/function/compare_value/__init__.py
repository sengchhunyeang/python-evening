# Compare three value
# find minimum value
def compare_value_noRe(val1, val2, val3):
    print("Minimum Value", min(val1, val2, val3))  # min() function find value smaller
    print("Maximum Value ", max(val2, val2, val3))  # max() find value bigger
# compare_value_noRe(1, 2, 3)
compare_value_noRe(2,34,3)
# for Developer
def compare_value_Re(val1, val2, val3):
    minimum = min(val1, val2, val3)
    maximum = max(val2, val2, val3)
    return f"minimum value:{minimum}\nmaximum value : {maximum}"
result = compare_value_Re(9, 10, 8)
print(result)

# Practice
# create function for checking
# odd number and even number
# odd = 1,3,5,7,9
# Even = 2,4,6,8