class Person:
    # a
    # Initialize Constructor
    def __init__(self, name, age, gender, job, company):
        self.name = name
        self.age = age
        self.gender = gender
        self.job = job
        self.company = company

    def getAllData(self):
        print(f"Name : {self.name}")
        print(" age :", self.age)
        print(" gender :", self.gender)
        print(" job :", self.job)
        print(" company :", self.company)



