# Import our own constants:
from globals import FOODMAX, STEPMAX, WIDTH, HEIGHT, X_MAX, Y_MAX, MS_TO_QUIT
from globals import FOOD as food, GHOSTS as ghosts

# Import our own doboggi_man class:
from characters import doboggi_man

import turtle
import math


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
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    @property
    def x1(self):
        return self.__x1

    @property
    def x2(self):
        return self.__x2

    @x1.setter
    def x1(self, x1):
        self.__x1 = x1

    @x2.setter
    def x2(self, x2):
        self.__x2 = x2

    def __add__(self, other):
        return Vector2D(self.x1 + other.x1, self.x2 + other.x2)

    def __sub__(self, other):
        return Vector2D(self.x1 - other.x1, self.x2 - other.x2)

    def __mul__(self, other):
        return Vector2D(self.x1 * other, self.x2 * other)

    def __str__(self):
        return f"{self.x1} {self.x2}"

    def length(self):
        return (self.x1 * self.x1 + self.x2 * self.x2) ** 0.5

    def normalized(self):
        length = self.length()
        return Vector2D(self.x1 / length, self.x2 / length)

    def tupled(self):
        return (self.x1, self.x2)

    @staticmethod
    def scalar_mult(v1, v2):
        return v1.x1 * v2.x1 + v1.x2 * v2.x2

    @staticmethod
    def angle(v1, v2):
        return math.acos(
            Vector2D.scalar_mult(v1, v2) / v1.length() / v2.length()
        )


print(Vector2D(1, 1).normalized().length())


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
        stopflag = False
        mvspd = 10
        for ghost in ghosts:
            position = Vector2D(*self.getPosition())
            coord = Vector2D(*ghost.getPosition())
            nxtcoord = Vector2D(*self.calc_ghost_path(coord.tupled(), 1))
            move_target = Vector2D(
                *self.getPosition()) + self.getPointingVector(food[0].getPosition()).normalized() * mvspd
            print((position - move_target).length())
            if checkCollision(nxtcoord.tupled(), move_target.tupled()):
                stopflag = True

        if not stopflag:
            self.ttl.forward(mvspd)
            self.face_coord(food[0].getPosition())

        #
        # Uncomment to dump positions in the PyCharm console window:
        #
        # print(ghosts[0], ghosts[1])
        # print(food[0], food[1], food[2])

    def calc_ghost_path(self, pos, shift):
        x, y = pos
        for i in range(shift):
            if x < -X_MAX - 25:
                x = X_MAX + 25
            else:
                x += -12 if shift > 0 else 12
        return (x, y)

    def face_coord(self, t):
        pos = self.getPosition()
        pointing_vector = Vector2D(*t) - Vector2D(*pos)
        angle = (
            (Vector2D.angle(pointing_vector, Vector2D(1, 0))) * 180 / math.pi
        )
        if pointing_vector.x2 < 0:
            angle = 360 - angle

        self.ttl.setheading(angle)

    def getPointingVector(self, t):
        pos = self.getPosition()
        return Vector2D(*t) - Vector2D(*pos)
