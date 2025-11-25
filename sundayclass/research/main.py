# Real Project: Student Management System with OOP & Modules (with comments)

## student.py

```python
class Student:
    def __init__(self, name, age, grade):
        # Initialize a student with name, age, and grade
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        # Display student's information
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
```

## student_manager.py

```python
from student import Student

class StudentManager:
    def __init__(self):
        # Initialize an empty list to store students
        self.students = []

    def add_student(self, name, age, grade):
        # Create a new student and add to the list
        student = Student(name, age, grade)
        self.students.append(student)
        print(f"Student {name} added.")

    def view_students(self):
        # Display all students in the list
        if not self.students:
            print("No students available.")
        for student in self.students:
            student.display_info()

    def delete_student(self, name):
        # Delete a student by name if exists
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"Student {name} deleted.")
                return
        print(f"Student {name} not found.")
```

## main.py

```python
from student_manager import StudentManager

# Create an instance of StudentManager
manager = StudentManager()

while True:
    # Menu for user operations
    print("\n1. Add Student\n2. View Students\n3. Delete Student\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        # Add a new student
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")
        manager.add_student(name, age, grade)
    elif choice == '2':
        # View all students
        manager.view_students()
    elif choice == '3':
        # Delete a student by name
        name = input("Enter name to delete: ")
        manager.delete_student(name)
    elif choice == '4':
        # Exit the program
        break
    else:
        # Invalid input
        print("Invalid choice")
```
