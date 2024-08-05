import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
bob = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
bob.shape('turtle')
# Set your turtle's speed using .speed(2)
bob.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
bob.color('green')
bob.pencolor('blue')
# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?
bob.forward(100)
# Move your turtle left or right using .left(90) or .right(90)
bob.right(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?
for i in range (4):
    bob.forward(100)
    bob.right(90)
# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
bob.goto(0, 0)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
bob.begin_fill()
bob.circle(50, steps=30)
bob.end_fill()
# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
# Draw 3 more shapes with different fill colors!
bob.goto(-10, -10)
bob.pencolor('red')
for i in range (4):
    bob.forward(50)
    bob.right(90)
bob.goto(-100, 100)
bob.color('yellow')
bob.begin_fill()
bob.circle(100, steps=30)
bob.end_fill()
bob.goto(-200, 100)
bob.color('purple')
for i in range (2):
    bob.forward(50)
    bob.right(90)
    bob.forward(100)
    bob.right(90)
# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
