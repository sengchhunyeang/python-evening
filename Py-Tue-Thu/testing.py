def hello(**kwargs):
    print("Hello",kwargs)
    for key,value in kwargs.items():
        print(f"{key}: {value}")
hello(email="emil123", age = 25, city = "Oslo", hobby = "coding")