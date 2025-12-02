def hello(**kwargs):
    print("Hello",kwargs)
    for key,value in kwargs.items():
        print(f"{key}: {value}")
hello(email="emil123", age = 25, city = "Oslo", hobby = "coding")

# Condition Statement
a = 40
b = 20

# find max of a and b
if a > b :
    print("maximum",a)
else:
    print("minimum",b)
