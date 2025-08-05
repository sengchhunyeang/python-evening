# Import the date class from the datetime module to work with dates
from datetime import date

# Define a class called Person to represent a person with a name, country, and date of birth
class Person:
    # Initialize the Person object with a name, country, and date of birth
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    
    # Calculate the age of the person based on their date of birth
    def calculate_age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

# Example usage
# Create three Person objects with different attributes
person1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
person3 = Person("Elizaveta Tilman", "USA", date(2000, 1, 1))

# Access and print the attributes and calculated age for each person
print("Person 1:")
print("Name:", person1.name)
print("Country:", person1.country)
# print("Date of Birth:", person1.date_of birth)
print("Age:", person1.calculate_age())

print("\nPerson 2:")
print("Name:", person2.name)
print("Country:", person2.country)
# print("Date of Birth:", person2.date_of birth)
print("Age:", person2.calculate_age())

print("\nPerson 3:")
print("Name:", person3.name)
print("Country:", person3.country)
# print("Date of Birth:", person3.date_of birth)
print("Age:", person3.calculate_age())
