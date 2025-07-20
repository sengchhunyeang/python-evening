#2- Caculator number arthmetic (+,-,*,/) result float all

value1= int(input("Input number1 :")) # default input() string convert to integer
value2= int(input("Input number2 :")) # covert string to int 

print(f"value:{value1} and value :{value2}")

add = value1 + value2
sub = value1 - value2
multiple = value1 * value2
dev = value1 / value2
# float() function convert all value to float 
print(f"{value1}+{value2}={float(add)}")
print(f"{value1}-{value2}={float(sub)}")

print(f"{value1}*{value2}={float(multiple)}")
print(f"{value1}/{value2}={float(dev)}")
