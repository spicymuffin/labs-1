"""
Name: Luigi Cussigh
Student ID: 2023148006
Lab problem: lab12_p5.py
"""

#
# Fraction class:
#


class Fraction(object):
    """
    Class to represent a number as a fraction

    Examples: 1/2, 2/5
    """

    def __init__(self, n, d):
        """Method to construct a Fraction object"""
        # Check that n and d are of type int:
        if type(n) != int or type(d) != int:
            raise ValueError("requires type int")
        # Check that denominator is non-zero:
        if d == 0:
            raise ZeroDivisionError("requires non-zero denominator")
        # If we get here, n and d are ok => initialize Fraction:
        self.num = n
        self.denom = d

    def __str__(self):
        """Returns a string representation of the fraction object (self)"""
        return str(self.num) + "/" + str(self.denom)

    def __mul__(self, other):
        """Returns new Fraction representing self * other"""
        if type(other) == Fraction:  # if fraction type
            new_num = self.num * other.num
            new_denom = self.denom * other.denom
        elif type(other) == int:  # if int type
            new_num = self.num * other
            new_denom = self.denom
        else:  # else raise error
            raise ValueError()
        return Fraction(new_num, new_denom)

    def __add__(self, other):
        """Returns new Fraction representing self + other"""
        if type(other) == Fraction:  # if fraction type
            new_num = self.num * other.denom + other.num * self.denom
            new_denom = self.denom * other.denom
        elif type(other) == int:  # if int type
            new_num = self.num + (self.denom * other)
            new_denom = self.denom
        else:  # else raise error
            raise ValueError()
        return Fraction(new_num, new_denom)

    def __float__(self):
        """Returns a float-value of the Fraction object"""
        return self.num / self.denom  # result of / is of type float
