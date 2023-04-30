import turtle


def drawSquare(myturtle, x, y, a):
    """draw square with turtle

    Args:
        myturtle (turtle object): turtle to be used
        x (int): x coord lower left corner
        y (int): y coord lower left corner
        a (int): square side length
    """
    myturtle.penup()
    myturtle.setposition((x, y))
    myturtle.pendown()
    myturtle.setheading(90)
    myturtle.forward(a)
    myturtle.right(90)
    myturtle.forward(a)
    myturtle.right(90)
    myturtle.forward(a)
    myturtle.right(90)
    myturtle.forward(a)
