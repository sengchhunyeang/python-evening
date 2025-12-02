def add_student():
    sid = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")

    with open("students.txt", "a") as f:
        f.write(f"{sid},{name},{age}\n")

    print("Student added successfully!")

def view_students():
    print("\n--- All Students ---")
    with open("students.txt", "r") as f:
        for line in f:
            sid, name, age = line.strip().split(",")
            print(f"ID: {sid}, Name: {name}, Age: {age}")
def search_student():
    find_id = input("Enter ID to search: ")
    found = False

    with open("students.txt", "r") as f:
        for line in f:
            sid, name, age = line.strip().split(",")
            if sid == find_id:
                print(f"Found → ID: {sid}, Name: {name}, Age: {age}")
                found = True
                break
    if not found:
        print("Student not found.")
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
