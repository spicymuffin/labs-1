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
    deg = 360//ringcnt  # calc displace (in deg)
    myturtle.hideturtle()  # hide turtle
    myturtle.pencolor("red")  # set bigger circles color
    for _ in range(ringcnt):  # draw a circle ringcnt times
        # turn right (could be left actually who cares why did i even write this if someone reads this please let me know or something)
        myturtle.right(deg)
        # draw circle
        myturtle.circle(r)

    # same stuff but blue
    myturtle.pencolor("blue")
    for _ in range(ringcnt):
        myturtle.right(deg)
        myturtle.circle(r//2)