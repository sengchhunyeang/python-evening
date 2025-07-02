# HomeWork
# Average Score of 5 Subject
# Problem:
# Write a Python program that:
# Takes input for 5 subject scores.
# Calculates the average score.
# Prints the average.
# Prints a message:
# If average ≥ 90 → "Excellent"
# If average ≥ 75 → "Very Good"
# If average ≥ 60 → "Good"

# print("input 5 subject : ")
# math = float(input("Math :"))
# english = float(input("English :"))
# khmer = float(input("Khmer :"))
# pysic = float(input("Pysic :"))
# Chemistry = float(input("Chemistry :"))
#
# # find average of subject 5
# score = math + english + khmer + pysic + Chemistry
# print("Total Score :", score)
# average = score / 5
# print("Total Average  :", average)
#
# if average >= 90:
#     print("Excellent")
# elif average >= 75:
#     print("Very Good")
# elif average >= 60:
#     print("Good")
# else:
#     print("Fail")


staff1= {"name" : "Seng Chhunyeang ", "salary":600,"Department":"IT"}
staff2= {"name" : " Panha Rith ", "salary":600,"Department":"Finance"}

salaryOfStaff1 = staff1["salary"]
salaryOfStaff2 = staff2["salary"]

if salaryOfStaff1 > salaryOfStaff2:
    print("higher salary :", staff1["name"],staff1["salary"])
elif salaryOfStaff1 == salaryOfStaff2:
    print("equal salary",salaryOfStaff1,"=",salaryOfStaff2)
else :
    print("higher salary :", staff2["name"],staff2["salary"])
