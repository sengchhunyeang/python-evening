def compare_value(value1, value2, value3):
    print("Minimum:", min(value1, value2, value3))
    print("Maximum:", max(value1, value2, value3))


def com_value(val1, val2, val3):
    maximum = max(val1, val2, val3)
    minimum = min(val1, val2, val3)
    return f"Maximum{maximum}Minimum{minimum}"


compare_value(1, 3, 4)
print(com_value(3, 4, 65))
