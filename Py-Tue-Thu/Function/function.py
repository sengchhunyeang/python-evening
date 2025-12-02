# function no parameter
def sum_value():
    a = 1
    b = 3
    print("Sum:", a + b)


# function has parameter
def sum_number(a, b):
    print("result :", a + b)


# sum_value()
#
# sum_number(a=1,b=2)
# sum_number(b=5,a=5)
# sum_number(b=10,a=4)

# Practice function has parameter
value1 = 10
value2 = 10
value3 = 10


# find value all which one maximum
def maximum(value1, value2, value_3):
    if value1 > value2 and value1 > value_3:
        max = value1
    elif value2 > value1 and value2 > value_3:
        max = value2

    elif value_3 > value1 and value_3 > value2:
        max = value_3
    else:
        max = "it equal "
    print("maximum of 3 value :", max)


maximum(value_1, value_2, value_3)
