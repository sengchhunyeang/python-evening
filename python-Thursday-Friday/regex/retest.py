import re

def get_valid_id():
    while True:
        user_id = input("Enter ID (numbers only): ")
        if re.fullmatch(r'\d+', user_id):
            return user_id
        else:
            print("Invalid ID. Please enter numbers only.")

def get_valid_name():
    while True:
        name = input("Enter Name (letters only): ")
        if re.fullmatch(r'[A-Za-z]+', name):
            return name
        else:
            print("Invalid Name. Please enter letters only.")

def get_valid_email():
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    while True:
        email = input("Enter Email: ")
        if re.fullmatch(email_pattern, email):
            return email
        else:
            print("Invalid Email format. Please try again.")

def main():
    try:
        user_id = get_valid_id()
        name = get_valid_name()
        email = get_valid_email()

        print("\nAll inputs are valid!")
        print(f"ID: {user_id}, Name: {name}, Email: {email}")

    except Exception as e:
        print(f"Unexpected Error: {e}")

if __name__ == "__main__":
    main()
