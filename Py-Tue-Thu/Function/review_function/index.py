#
def value(*args):
    print(type(args))
    print("value:", )


def greeting(name, *args):
    print("name:", name, "\nAllData :", args)


# breaking Line


greeting("Seng ChhunYeang", "35", "address", "Work", "Position")


# **kwargs
def book(**kwargs):
    print(type(kwargs))
    print(kwargs)


# dictionaries
book(language="Python", study="4month", price="120$")

# value(1,2)
# value(1,2,3)
# value(1,"book",True)

# Practice
# arbitrary argument for sum this value in list
number = [1, 23, 4, 4, 5, 6, 6, 7]


def sum_list(*param):
    print(type(param))
    return sum(param)

print(sum_list(*number))
print(sum_list(1,2,3,6,7,8,9))
