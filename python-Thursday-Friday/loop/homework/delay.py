import time  # Import the time module

attempts = 0
while attempts < 3:
    password = input("password: ")
    if password == "hello":
        print("password is correct")
        break  # Exit the loop if password is correct
    else:
        print("password is incorrect, try again...")
        if attempts < 2:  # Only delay if not the last attempt
            print("Waiting 3 seconds before next attempt...")
            time.sleep(3)  # 3-second delay
    attempts += 1