"""
Name: Luigi Cussigh
Student ID: 2023148006
Lab problem: lab13_p1.py
"""


class Range:
    """class that represents a range"""

    def __init__(self, start, end):
        """initialize range object

        Args:
            start (int): range start
            end (int): range end
        """
        # raise index error if
        # bounds are messed up
        if not (start <= end):
            raise IndexError

        self.__start = start  # set start
        self.__end = end  # set end

    def __str__(self):
        """returns stringified range object

        Returns:
            str: stringified range object
        """
        # returns stringified range object
        return f"{self.__start}...{self.__end}"

    def __lt__(self, other):
        """compares range objects with operator <

        Args:
            other (range object): range object we are comparing with

        Returns:
            bool: operation result
        """
        if self.__end < other.__start:
            # if self's end is smaller
            # than the other's end
            return True  # return true
        return False  # else return false
