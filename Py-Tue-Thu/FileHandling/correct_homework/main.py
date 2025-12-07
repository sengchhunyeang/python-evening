
from time import sleep
from Moudule import *
import data
while True:
    option_student_list()
    print("==============================")
    opt = int(input("Pls chose option :"))
    if opt == 1:
        print("Add New student ")
        # call function
        data.student_id = int(input("student id :"))
        data.student_name = input("student name :")
        data.student_age = int(input("student age :"))
        new_student(data.student_id,data.student_name,data.student_age)
    elif opt == 2:
        print("view student record ")
        view_students()
    elif opt == 3 :
        print("Search Student By Id")
        search_student()
    else :
        print("System exiting... ")
        sleep(2)
        break