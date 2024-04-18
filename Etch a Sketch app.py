import turtle

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

# Setup
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed to maximum

# Keyboard bindings
turtle.listen()
turtle.onkeypress(move_forward, 'Right')
turtle.onkeypress(move_backward, 'Left')
turtle.onkeypress(turn_left, 'Up')
turtle.onkeypress(turn_right, 'Down')
turtle.onkeypress(clear_screen, 'c')

# Keep the window open
turtle.mainloop()
