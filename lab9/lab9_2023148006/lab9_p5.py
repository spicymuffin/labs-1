#
# Please save this program to the hard-drive of your computer and set
# it up as a PyCharm project.
#

import turtle


def square(t, length):  # draws a square
    for s in range(4):
        t.forward(length)
        t.left(90)


def writeText():
    text_t.clear()  # clear previous text
    posx, posy = t.position()  # assign coord vars
    posx = int(posx)  # get x coord of turtle
    posy = int(posy)  # get y coord of turtle
    text_t.write(f"({posx}, {posy})", font=(
        'Times New Roman', 8, 'bold'))  # actually write the text
    text_t.setpos(0, 0)  # set text position


def closeDown():
    turtle.bye()  # exit


def drawShape(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    t.begin_fill()
    if x <= 100:  # Left third:
        t.color("green")
        square(t, 10)
    elif 100 < x <= 200:  # Middle third:
        t.color("red")
        t.circle(10)
    else:
        t.color("blue")
        square(t, 10)
    t.end_fill()

#
# main:
#


# Set window to be 300 x 200 with the point (0, 0) as the lower-left
# corner and (300, 200) as the upper right corner:
turtle.setup(300, 200)
turtle.screensize(300, 200)
turtle.setworldcoordinates(0, 0, 300, 200)

# Initialize global turtle t variable which will be used inside
# of the handler functions:
t = turtle.getturtle()
t.speed(0)  # Set fastest screen update speed for this turtle.

text_t = turtle.Turtle()  # get text turtle reference
text_t.speed(0)  # Set fastest screen update speed for text turtle.

# Draw two vertical lines to divide the window into thirds:
t.penup()
t.setpos(100, 0)  # First line
t.pendown()
t.setpos(100, 200)
t.penup()
t.setpos(200, 0)  # Second line
t.pendown()
t.setpos(200, 200)


# Register callback for key-press events:
turtle.onkey(writeText, 'Up')
turtle.onkey(closeDown, 'q')
# Register callback for mouse on-click events:
turtle.onscreenclick(drawShape)
# Enter event loop:
turtle.listen()
turtle.mainloop()
