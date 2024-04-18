import turtle
import math
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Amazing Spirograph")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed
t.pensize(2)  # Set the pen size

# Function to draw a spirograph pattern
def draw_spirograph(radius, gap):
    for angle in range(0, 360, gap):
        # Set a random color
        r = random.random()
        g = random.random()
        b = random.random()
        t.color(r, g, b)
        
        # Calculate coordinates for the spirograph pattern
        x = radius * math.sin(math.radians(angle))
        y = radius * math.cos(math.radians(angle))
        
        # Move the turtle to the calculated coordinates
        t.penup()
        t.goto(x, y)
        t.pendown()
        
        # Draw a circle at the current position
        t.circle(50)

# Draw the spirograph
draw_spirograph(100, 5)

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
