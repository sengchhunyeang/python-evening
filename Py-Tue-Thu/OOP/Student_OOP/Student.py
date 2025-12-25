### **Create a Class and Object**


# - **Task:**
# Create a class Student with attributes name, gender, subject, classroom.
# Create an object and print out the attributes.
# How to create a class
class Student:
    # Attribute , Propertice
    # Method
    # How to add student
    # Construtor is Special Method
    def __init__(self, name, gender, subject, classroom):
        self.name = name
        self.gender = gender
        self.subject = subject
        self.classroom = classroom

    def get_student(self):
        print(
            f"student name:{self.name}\nstudent gender :{self.gender}\nsubject:{self.subject}\nclassroom:{self.classroom}"
        )


# How to crate object
personName = "Chhunyeang"
personGender = "Male"
personSubject = "Python"
classRoom = "RoomB"
# Create student
student = Student(
    name=personName, gender=personGender, subject=personSubject, classroom=classRoom
)
# get data student

student.get_student()
