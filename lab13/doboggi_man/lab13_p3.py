
# Import our own constants:
from globals import FOODMAX, STEPMAX, WIDTH, HEIGHT, X_MAX, Y_MAX, MS_TO_QUIT
from globals import FOOD as food, GHOSTS as ghosts

# Import our own doboggi_man class:
from characters import doboggi_man

import turtle

def checkCollision(t1, t2):
        """checks whether two coord tuples are sufficiently close (collide)
           i did steal this code, sue me

        Args:
            t1 (tuple): coord 1
            t2 (tuple): coord 2

        Returns:
            bool: whether collides or not
        """
        if (abs(t1[0] - t2[0]) < 25) and (abs(t1[1] - t2[1]) < 25):
            return True
        return False

class Vector2D:
    def __init__(self, a, b) -> None:
        self.__a = a
        self.__b = b

    def __sub__(self, other):
        return Vector2D(self.__a - other.__a, self.__b - other.__b)

    def __str__(self):
        return f"{self.__a} {self.__b}"

print(Vector2D(1, 1) - Vector2D(-1, -1))


class auto_doboggi_man(doboggi_man):

    """
    Class auto_doboggi_man, the autonomous doboggi-collector.

    The auto_doboggi_man class is a subclass of the doboggi_man class. It
    inherits all data attributes and methods from the doboggi_man class. It
    overrides the move() method of the doboggi_man class to automatically
    navigate doboggi_man across the screen.

    Attributes:
    ... Please describe your attributes here
    """

    def move(self):
        #
        # Change this code to make your doboggi_man navigate the screen
        # and collect all doboggi.

        for ghost in ghosts:
            coord = ghost.getPosition()
            nxtcoord = self.getNxtFrameGhostCoord(coord)

        #
        # Uncomment to dump positions in the PyCharm console window:
        #
        print(ghosts[0], ghosts[1])
        print(food[0], food[1], food[2])

    def getNxtFrameGhostCoord(t):
        if t[0] < -X_MAX - 25:
            return (X_MAX + 25, t[1])
        else:
            return (t[0]+12, t[1])

    def faceCoord(t):
        pass