# Traffic Light Simulation

print("===== Traffic Light Simulation =====")

# Get user input
color = input("Enter traffic light color (red, yellow, green): ").lower()

# Check the color and give action
if color == "red":
    action = "Stop!"
elif color == "yellow":
    action = "Get ready to move!"
elif color == "green":
    action = "Go!"
else:
    action = "Invalid color! Please enter red, yellow, or green."

# Print result
print(f"Traffic light is {color}. Action: {action}")
