while True:
    try:
        num = int(input("Enter a number: "))
        break  # Exit the loop if input is valid
    except ValueError:  # Correct exception for invalid int conversion
        print("Invalid input. Please enter a valid number.")