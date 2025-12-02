##Find value all , which one is maximum

def max (a, b, c):
    if a > b and a >c:
        max = a
    elif b > a and b > c:
        max = b
    elif c > a and c > b:
        max = c
    print("max of 3 value:", max)


max(15,23,78)
