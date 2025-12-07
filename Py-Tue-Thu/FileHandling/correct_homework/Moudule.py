# option function
def option_student_list():
    print("1- add new student ")
    print("2- View student ")
    print("3- Search by ID student ")
    print("4- Exit list Student ")


# add new student function write file
def new_student(student_id, student_name, student_age):
    with open("database_student.txt", "a") as file:
        file.write(f"{student_id},\t{student_name},\t{student_age}\n")
    print("student added successfully!")


# view data_student in txt
def view_students():
    print("\n--- All Students ---")
    with open("database_student.txt", "r") as f:
        for line in f:
            sid, name, age = line.strip().split(",")
            print(f"ID: {sid}, Name: {name}, Age: {age}")




def search_student():
    find_id = input("Enter ID to search: ")
    found = False

    with open("database_student.txt", "r") as f:
        for line in f:
            sid, name, age = line.strip().split(",")
            if sid == find_id:
                print(f"Found → ID: {sid}, Name: {name}, Age: {age}")
                found = True
                break

    if not found:
        print("Student not found.")


