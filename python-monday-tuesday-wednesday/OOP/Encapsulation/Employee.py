class Employee:
    def __init__(self, emp_name=None, emp_salary=0):
        self.__emp_name = emp_name
        self.__emp_salary = emp_salary

    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name

    def set_emp_salary(self, emp_salary):
        self.__emp_salary = emp_salary


    def getter(self):
     return f"Employee name :{self.__emp_name}\nEmployee salary :{self.__emp_salary}$"


obj = Employee()
obj.set_emp_name("chhunyeang")
obj.set_emp_salary(400)
print(obj.getter())
