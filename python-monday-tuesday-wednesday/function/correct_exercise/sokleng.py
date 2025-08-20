RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_GREEN = "\033[1;32m"
LIGHT_PURPLE = "\033[1;35m"
END = "\033[0m"


# Define a function in python that accepts 3 value and returns the maximum of three numbers.
def maxi_value (a, b, c):
    while True:
        try:
            print("="*20,f"{LIGHT_BLUE}Please input your value below to check which maximum value.{END}","="*20)
            a = int(input("Please input value of a: "))
            b = int(input("Please input value of b: "))
            c = int(input("Please input value of c: "))
            print("="*20,f"{LIGHT_GREEN}Result after check maximum value the user inputed.{END}","="*20)
            if a > b and a > c:
                return a
            elif b > a and b > c:
                return b
            else:
                return c
        except:
            print("="*20,f"{RED}Error Info !!!{END}","="*20)
            print(f"{RED}Invalid input. Please enter numeric values.{END}")

print(f"The maximum value that you inputed is: {GREEN}{maxi_value(0, 0, 0)}{END}")


# Define a function that accepts lowercase words and returns the uppercase words.
def Conv_upper (text):
    while True:
        try:
            print("="*20,f"{LIGHT_BLUE}Please input lowercase word that you want to convert.{END}","="*20)
            text = input("Please input your lowercase word: ")
            if not text.islower():
                print("="*20,f"{RED}Error Info !!!{END}","="*20)
                print(f"{RED}Please input lowercase letters only !!!{END}")
            else:
                print("="*20,f"{LIGHT_GREEN}Result after convert your word.{END}","="*20)
                return text.upper()
        except:
            print("="*20,f"{RED}Error Info !!!{END}","="*20)
            print(f"{RED}Invalid input. Please enter lowercase letters only.{END}")

print(f"The uppercase word after converted is: {GREEN}{Conv_upper(0)}{END}")


# Define a function that accepts a number and returns whether the number is even or odd.
def even_odd (num):
    while True:
        try:
            print("="*20,f"{LIGHT_BLUE}Please input a number that you want to check.{END}","="*20)
            num = int(input("Please input your number: "))
            print("="*20,f"{LIGHT_GREEN}Result after check your number.{END}","="*20)
            if num % 2 == 0:
                return "Even"
            else:
                return "Odd"
        except:
            print("="*20,f"{RED}Error Info !!!{END}","="*20)
            print(f"{RED}Invalid input. Please enter numeric values.{END}")

print(f"The number that you inputed is: {GREEN}{even_odd(0)}{END}")