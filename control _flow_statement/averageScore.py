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




# Take input for 5 subjects
s1 = float(input("Enter score for subject 1: "))
s2 = float(input("Enter score for subject 2: "))
s3 = float(input("Enter score for subject 3: "))
s4 = float(input("Enter score for subject 4: "))
s5 = float(input("Enter score for subject 5: "))

# Calculate average
average = (s1 + s2 + s3 + s4 + s5) / 5

# Print average
print("Average score:", average)

# Print message
if average >= 90:
    print("Excellent")
elif average >= 75:
    print("Very Good")
elif average >= 60:
    print("Good")
