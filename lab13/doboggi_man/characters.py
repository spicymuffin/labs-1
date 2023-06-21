
# Import our own constants:
from globals import FOODMAX, STEPMAX, WIDTH, HEIGHT, X_MAX, Y_MAX, MS_TO_QUIT

import turtle


class thing:
    """
    Root class.

    Attributes:
    ttl (turtle.Turtle): turtle object
    phase (int): phase used to flip appearance of animated screen objects
    """

    def __init__(self, x=0, y=0):
        """
        Special method to initialize a 'thing' object in memory.
        The 'self' parameter refers to the object.
        The 'x' and 'y' parameters define the screen position (x, y).
        NOTE: in the __init__() methods of the child-classes we also
              call this method to set up the screen coordinates. (The child
              inherits these data attributes from the parent, so we use the
              parent's __init__() method for initialization.
        """
        self.ttl = turtle.Turtle()  # create a new Python turtle object
        self.ttl.penup()
        self.ttl.speed('fastest')
        self.ttl.goto(x, y)
        self.phase = 0

    def getPosition(self):
        """
        Method to return the screen position of a 'thing' object.
        The return-value is a tuple (x, y).
        """
        # Retrieve coordinates from turtle ttl and return tuple:
        return (self.ttl.xcor(), self.ttl.ycor())


class doboggi(thing):
    """
    Doboggi class for representing food in the game.

    The doboggi class is a sub-class of the 'thing' class. Therefore, it
    inherits all data attributes and methods from the 'thing' class.
    """

    def __init__(self, x=0, y=0):
        """Special method to initialize a 'doboggi' object in memory."""
        thing.__init__(self, x, y)  # Call __init__() of the superclass
        self.ttl.shape('img/doboggi.gif')  # Set image of the object's turtle

    def setIsEaten(self):
        """
        Stop displaying this doboggi object in the game.
        """
        self.ttl.hideturtle()

    def __str__(self):
        """
        Special method for displaying a doboggi object.

        Python calls this method whenever it wants to show an object.
        For example, if d is a doboggi object, print(d) will make a call
        to __str__(). The string returned by __str__ will be printed.
        """
        # Note: we call the getPosition() method which the doboggi class
        # inherits from the thing class to retrieve its own position.
        return 'Doboggi' + str(self.getPosition())


class ghost(thing):
    """
    Class to represent ghost objects in the game.

    The ghost class is a sub-class of the 'thing' class. Therefore, it
    inherits all data attributes and methods from the 'thing' class.
    """

    def __init__(self, name, x=0, y=0):
        """Special method to initialize a ghost object."""
        thing.__init__(self, x, y)  # Call __init__ of the superclass
        self.ttl.left(180)
        self.name = name            # Initialize the name data attribute


    def updateShape(self):
        """
        This method switches the ghost object's turtle between two different
        images to give the impression of the ghost moving its legs. You can
        view the two gif images in any image viewer, for example the open-
        source gimp image editor.
        """
        if self.phase == 0:
            self.ttl.shape('img/ghost_phase_0.gif')
            self.phase = 1
        else:
            self.ttl.shape('img/ghost_phase_1.gif')
            self.phase = 0

    def move(self):
        """
        Move a ghost right-to-left on the screen. If the ghost left the screen
        at the left border, it is placed to the right of the right border to
        re-enter the game.
        """
        if self.ttl.xcor() < -X_MAX - 25:
            self.ttl.setx(X_MAX + 25)
        else:
            self.ttl.forward(12)

    def __str__(self):
        """
        Special method for displaying a ghost object.
        Python calls this method whenever it wants to show an object.
        For example, if g is a ghost object, print(g) will make a call
        to __str__(). The string returned by __str__ will be printed.
        """
        # Note: we call the getPosition() method which the ghost class
        # inherits from the thing class to retrieve its own position.
        return 'Ghost ' + self.name + str(self.getPosition())


class doboggi_man(thing):
    """
    Class to represent the doboggi_man object in the game.

    Attributes:
    dir (string): direction doboggi_man is facing ('east', 'west', 'south', or
                  'north').
    steps (integer): number of remaining steps until the game ends.
    isYum (Boolean): controls the "Yum" cartoon bubble.
    isYumOff(Boolean): another control variable for the "Yum" cartoon bubble.
    """

    def __init__(self, x=0, y=0):
        """Special method to initialize a doboggi_man object"""
        thing.__init__(self, x, y)  # call __init__() of the superclass
        self.dir = 'east'           # set initial direction
        self.steps = STEPMAX        # remaining steps
        self.isYum = False          # no
        self.isYumOff = False       # bubble

    def updateShape(self):
        """
        Method to control the appearance of doboggi_man.

        The appearance can be either the "Yum" bubble or the doboggi_man image
        (open or closed) facing any of the four directions.

        The open versus closed doboggi_man image is controlled by the 'phase'
        data attribute (inherited from the 'thing' class).
        """
        if self.isYumOff:
            self.isYumOff = False
            self.isYum = False
        if self.isYum:
            self.isYumOff = True
            self.ttl.shape('img/yum.gif')
            turtle.update()
            return
        if self.phase == 0:
            if self.dir == 'east':
                self.ttl.shape('img/dbm_east_phase_0.gif')
            elif self.dir == 'west':
                self.ttl.shape('img/dbm_west_phase_0.gif')
            elif self.dir == 'north':
                self.ttl.shape('img/dbm_north_phase_0.gif')
            else:
                self.ttl.shape('img/dbm_south_phase_0.gif')
            self.phase = 1
        else:
            if self.dir == 'east':
                self.ttl.shape('img/dbm_east_phase_1.gif')
            elif self.dir == 'west':
                self.ttl.shape('img/dbm_west_phase_1.gif')
            elif self.dir == 'north':
                self.ttl.shape('img/dbm_north_phase_1.gif')
            else:
                self.ttl.shape('img/dbm_south_phase_1.gif')
            self.phase = 0

    def move(self):
        """Method to move doboggi_man across the screen."""
        # Don't move beyond screen border:
        if self.dir == 'east' and self.ttl.xcor() > X_MAX:
            return
        if self.dir == 'west' and self.ttl.xcor() < -X_MAX:
            return
        if self.dir == 'north' and self.ttl.ycor() > Y_MAX:
            return
        if self.dir == 'south' and self.ttl.ycor() < -Y_MAX:
            return
        # Move forward:
        self.ttl.forward(10)

    def getRemainingSteps(self):
        """Return the steps left until the game terminates"""
        return self.steps

    def decrementSteps(self):
        """Decrement remaining steps by 1"""
        self.steps -= 1

    def turnEast(self):
        """Turn doboggi_man's direction to the east."""
        if self.dir == 'east':  # do nothing if already facing east
            return
        self.ttl.setheading(0)  # change doboggi_man turtle's direction to east
        self.dir = 'east'  # remember our new direction
        self.updateShape()  # call to switch image according our new direction

    def turnSouth(self):
        """Ditto for south"""
        if self.dir == 'south':
            return
        self.ttl.setheading(270)
        self.dir = 'south'
        self.updateShape()

    def turnWest(self):
        """Ditto for west"""
        if self.dir == 'west':
            return
        self.ttl.setheading(180)
        self.dir = 'west'
        self.updateShape()

    def turnNorth(self):
        """Ditto for north"""
        if self.dir == 'north':
            return
        self.ttl.setheading(90)
        self.dir = 'north'
        self.updateShape()

    def setIsYum(self):
        """
        Remember to display the "Yum" bubble and call
        updateShape() to switch doboggi_man's appearance.
        """
        self.isYum = True
        self.updateShape()
