# Exercise 4: Temperature Classifier
# Classify temperature:

# Below 0: Freezing

# 0-15: Cold

# 16-25: Moderate

# 26-35: Hot

# Above 35: Very Hot

# Example:
# python
temp = float(input("Enter temperature: "))
if temp < 0:
    print("Freezing")
elif 0 <= temp <= 15:
    print("Cold")
elif 16 <= temp <= 25:
    print("Moderate")
elif 26 <= temp <= 35:
    print("Hot")
else:
    print("Very Hot")