answer = "yes"
while answer == "yes":
    print("Hello!")
    answer = input("Say again? (yes/no): ")


    def greet(name, message):
        print(f"{message}, {name}!")


    greet("Alice", "Hello")  # Output: Hello, Alice!