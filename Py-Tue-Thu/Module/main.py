from caculator import *

import student

student.student_name = input("Student name :")
student.java = float(input("Enter Score Java :"))
student.python = float(input("Enter score python :"))
student.javaScript = float(input("Enter score JavaScript:"))

# call Student average function from calculator file module 
result_average = average(student.java,student.python,student.javaScript)

print("student name :",student.stdent_name)
print("Get Average :",result_average)

grade(result_average)