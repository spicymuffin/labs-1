# Import our own constants:
from globals import FOODMAX, STEPMAX, WIDTH, HEIGHT, X_MAX, Y_MAX, MS_TO_QUIT
from globals import FOOD as food, GHOSTS as ghosts

# Import our own doboggi_man class:
from characters import doboggi_man

import turtle
import math


# omg writing up docs for this is going to take a TON of time help


def check_collision(t1, t2):
    """checks whether two coord tuples are sufficiently close (collide)
       i did steal this code, sue me

    Args:
        t1 (tuple): coord 1
        t2 (tuple): coord 2

    Returns:
        bool: whether collides or not
    """
    if (abs(t1[0] - t2[0]) < 25) and (abs(t1[1] - t2[1]) < 25):
        return True  # collides
    return False  # doesnt collide


class Vector2D:
    """2D vector handling class, can also store positions (really handy)"""

    def __init__(self, x1, x2):
        """intiate a Vector2D by giving an x and y coordinate

        Args:
            x1 (float or int): x
            x2 (float or int): y
        """
        self.x1 = x1  # set x
        self.x2 = x2  # set y

    @property
    def x1(self):
        """x1 getter"""
        return self.__x1  # get x1

    @property
    def x2(self):
        """x2 getter"""
        return self.__x2  # get x2

    @x1.setter
    def x1(self, x1):
        """x1 setter"""
        self.__x1 = float(x1)  # set x1

    @x2.setter
    def x2(self, x2):
        """x2 setter"""
        self.__x2 = float(x2)  # set x2

    def __add__(self, other):
        """defines addition operation for two v2ds"""
        return Vector2D(self.x1 + other.x1, self.x2 + other.x2)  # return v2d

    def __sub__(self, other):
        """defines subtraction operation for two v2ds"""
        return Vector2D(self.x1 - other.x1, self.x2 - other.x2)  # return v2d

    def __mul__(self, other):
        """defines multiplication by scalar operation for v2ds"""
        return Vector2D(self.x1 * other, self.x2 * other)  # return v2d

    def __rmul__(self, other):
        """defines multiplication by scalar operation for v2ds"""
        return Vector2D(self.x1 * other, self.x2 * other)  # return v2d

    def __str__(self):
        """defines how a v2d should be converted to a string"""
        return f"({self.x1}, {self.x2})"  # str-ified

    def __repr__(self):
        """defines how a v2d should be converted to a string"""
        return f"({self.x1}, {self.x2})"  # str-ified

    def length(self):
        """returns length of v2d"""
        return (self.x1 * self.x1 + self.x2 * self.x2) ** 0.5  # length

    def normalized(self):
        """returns new normalized vector with same direction as caller v2d"""
        length = self.length()  # get lenth
        return Vector2D(self.x1 / length, self.x2 / length)  # scale coords

    def tupled(self):
        """retruns x1, x2 in a tuple"""
        return (self.x1, self.x2)  # return tuple

    @staticmethod
    def scalar_mult(v1, v2):
        """return standard scalar multiplication of two v2ds"""
        return v1.x1 * v2.x1 + v1.x2 * v2.x2  # return result

    @staticmethod
    def angle(v1, v2):
        """find angle between two v2ds"""
        # return result (radians)
        return math.acos(
            Vector2D.scalar_mult(v1, v2) / v1.length() / v2.length()
        )

    @staticmethod
    def distance(v1, v2):
        """find distance between two v2ds (if they represent coords)"""
        return (v1 - v2).length()  # return result obv


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
        """moves doboggi_man to victory"""

        # movespeed
        mvspd = 10

        # init closest ghost (ghost we will avoid)
        ghost = ghosts[0]
        # find closest ghost
        ghost = self.find_closest_thing(ghosts)
        # get closest ghosts position
        ghost_pos = Vector2D(*ghost.getPosition())

        # init target to move to
        target = Vector2D(*food[0].getPosition())
        # find closest food
        f = self.find_closest_thing(food)
        # set target to closest food's position
        target = Vector2D(*f.getPosition())

        # calcualte ghost path 5 steps in time
        ghost_path = self.calc_ghost_path(ghost_pos, -1, 3)

        # predict self's position in next step
        self_predicted = (
            Vector2D(*self.getPosition())
            + self.get_pointing_vector(target).normalized() * mvspd
        )

        # get pointing vector to target
        pointing_vector = self.get_pointing_vector(target)

        # determine whether moving to predicted position collides
        # with any of the positions in the ghost's path

        # iterate through path
        for i in range(len(ghost_path)):
            # check if collides with position in path
            if check_collision(
                ghost_path[i].tupled(), self_predicted.tupled()
            ):
                # get pointing vector directed in the
                # opposite direction of the ghost
                pointing_vector = -1 * self.get_pointing_vector(ghost_path[i])
                break

        # set self's direction (is determined by ghost positions)
        self.match_pointing_vector(pointing_vector)
        # move self in that direction
        self.ttl.forward(mvspd)

        # i want doboggi_man to rotate
        remsteps = self.getRemainingSteps()  # im having fun
        if remsteps % 4 == 0:  # rotate to direction based on
            self.turnEast()  # the number of steps remaining
        elif remsteps % 4 == 1:  # if remainder is 1 set east
            self.turnNorth()
        elif remsteps % 4 == 2:  # and so on
            self.turnSouth()
        elif remsteps % 4 == 3:
            self.turnWest()  # 😅

    def predict_ghost_position(self, pos, shift):
        """predicts ghost position [shift] steps ahead

        Args:
            pos (v2d or tuple): current ghost position
            shift (int): step shift

        Raises:
            ValueError: if pos isnt a tuple or v2d

        Returns:
            v2d: predicted ghost position
        """
        x = y = 0  # init vars
        if type(pos) == tuple:
            x, y = pos  # unpack tuple if tuple
        elif type(pos) == Vector2D:
            x = pos.x1
            y = pos.x2  # unpack v2d if v2d
        else:
            raise ValueError  # raise error if not both

        s = 1 if shift > 0 else -1  # determine shift sign
        shift = abs(shift)  # shift is used as the loop iter count

        for _ in range(shift):  # iter through steps
            if x < -X_MAX - 25:  # this is the code that drives the ghosts
                x = X_MAX + 25  # ripped from provided code
            else:
                x += -12 if s > 0 else 12  # except we can move backwards
        return Vector2D(x, y)  # return predicted position

    def calc_ghost_path(self, pos, start_shift, end_shift):
        """calculates ghost path from [curr_step + start_shift] to
        [curr_step + end_shift]

        Args:
            pos (tuple or v2d): current ghost position
            start_shift (int): step shift start
            end_shift (int): step shift end

        Returns:
            list of v2d: path
        """
        path = []  # init list
        for i in range(start_shift, end_shift + 1):  # iter through steps
            predicted_position = self.predict_ghost_position(
                pos, i
            )  # predict pos at step
            path.append(predicted_position)  # append to path
        return path  # return path

    def find_closest_thing(self, things):
        """finds closest [thing] from list [things]

        Args:
            things (list of [thing]): list to search

        Returns:
            thing: closest thing to self
        """
        closest = things[0]  # init closest thing
        self_pos = Vector2D(*self.getPosition())  # get self's position
        mindst = dst = Vector2D.distance(
            Vector2D(*things[0].getPosition()), self_pos
        )  # init minimal distance
        for t in things:  # iterate through things
            pos = Vector2D(*t.getPosition())  # thing's position
            dst = Vector2D.distance(pos, self_pos)  # distance to that thing
            if mindst > dst:  # update minimal dist and thing
                closest = t
                mindst = dst

        return closest  # return closest thing

    def match_pointing_vector(self, v):
        """rotates ttl to match direction of [v]

        Args:
            v (v2d): v2d to match the direction of
        """
        angle = (
            (Vector2D.angle(v, Vector2D(1, 0))) * 180 / math.pi
        )  # find angle between Ox and v
        if v.x2 < 0:  # maps angle to [0, 360)
            angle = 360 - angle

        self.ttl.setheading(angle)  # rotate ttl

    def get_pointing_vector(self, t):
        """get a vector that points to coordinate t

        Args:
            t (v2d or tuple): coordinate to point to

        Raises:
            ValueError: if t isnt a v2d or tuple

        Returns:
            v2d: pointing vector
        """
        pos = self.getPosition()  # get self's position
        if type(t) == tuple:  # unpack tuple if tuple
            return Vector2D(*t) - Vector2D(*pos)
        elif type(t) == Vector2D:  # unpack v2d if v2d
            return t - Vector2D(*pos)
        else:  # raise error if not both
            raise ValueError
