from turtle import *

speed(0)        # Fastest drawing speed
bgcolor('black') # Black background
color('orange')  # Orange drawing color
hideturtle()     # Hide the turtle cursor

n = 1
p = True

while True:
    circle(n)    # Draw a circle with radius 'n'
    if p:
        n = n - 1  # Decrease radius
    else:
        n = n + 1  # Increase radius
    if n == 0 or n == 60:  # Reverse direction at limits
        p = not p
    left(1)      # Slight turn
    forward(3)   # Move forward slightly