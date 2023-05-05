import turtle


def drawFlower(myturtle, r):
    """ Draws a flower composed of 24 circles
    on the screen: 12 red circles and 12
    blue circles. The radius of the red
    circles is "r". The radius of the
    blue circles is half of "r".
    The turtle "myturtle" is already
    positioned in the center of the flower.
    """
    ringcnt = 12
    deg = 360//ringcnt
    myturtle.hideturtle()
    myturtle.pencolor("red")
    for i in range(ringcnt):
        myturtle.right(deg)
        myturtle.circle(r)

    myturtle.pencolor("blue")
    for i in range(ringcnt):
        myturtle.right(deg)
        myturtle.circle(r//2)


# screen size
screen_width = 600
screen_height = 600
turtle.setup(screen_width, screen_height)

# create turtle window
window = turtle.Screen()
window.title('flower')

t = turtle.Turtle()
t.speed(0)
drawFlower(t, 125)

window.exitonclick()
