import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spirograph")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed
t.pensize(2)  # Set the pen size

# Function to draw a spirograph
def draw_spirograph(size, gap):
    for _ in range(int(360 / gap)):
        t.color("pink")
        t.circle(size)
        t.left(gap)

# Draw the spirograph
draw_spirograph(100, 10)

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
