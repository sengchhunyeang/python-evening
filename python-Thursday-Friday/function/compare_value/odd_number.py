def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"
print(check_even_odd(7))
number = input("Enter number :")
con_number = int(number)
print(type(con_number))
print(check_even_odd(con_number))
