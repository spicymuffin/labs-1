"""
Name: Luigi Cussigh
Student ID: 2023148006
Lab problem: lab12_p4.py
"""

#
# Fraction class:
#


class Fraction(object):
    """
    Class to represent a number as a fraction

    Examples: 1/2, 2/5
    """

    def reduce(self):
        """
        Reduces self to simplest terms. This is done by dividing both
        numerator and denominator by their greatest common divisor (GCD).
        Also removes the signs if both numerator and denominator are
        negative. Whole numbers (1, 2, ...) are represented as
        1/1, 2/1, 3/1, ...
        """

        def find_gcd(a, b):
            """finds gcd of a and b

            Args:
                a (int): input 1
                b (int): input 2

            Returns:
                int: gcd
            """
            gcd = 0
            while a != 0 or b != 0:  # while we dont get down to zero
                a = a % b
                if a == 0:
                    gcd = b  # gcd is b
                    break
                b = b % a
                if b == 0:
                    gcd = a  # gcd is a
                    break
            return gcd  # return gcd

        gcd = find_gcd(self.num, self.denom)  # find gcd

        # divide entire fraction by gcd
        self.num //= gcd
        self.denom //= gcd

        if self.num < 0 and self.denom < 0:
            self.num *= -1  # flip signs
            self.denom *= -1  # im so tired of leavin these comments

    def adjust(self, factor):
        """multiplies numerator and denominator by factor

        Args:
            factor (int): factor
        """
        self.num *= factor  # multiply
        self.denom *= factor

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
        self.reduce()  # reduce fraction

    def __str__(self):
        """Returns a string representation of the fraction object (self)"""
        return str(self.num) + "/" + str(self.denom)

    def __mul__(self, other):
        """Returns new Fraction representing self * other"""
        new_num = self.num * other.num
        new_denom = self.denom * other.denom  # mult denom
        return Fraction(new_num, new_denom)

    def __add__(self, other):
        """Returns new Fraction representing self + other"""
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom  # calc new denum
        return Fraction(new_num, new_denom)

    def __float__(self):
        """Returns a float-value of the Fraction object"""
        return self.num / self.denom  # result of / is of type float
