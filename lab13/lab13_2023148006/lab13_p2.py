"""
Name: Luigi Cussigh
Student ID: 2023148006
Lab problem: lab13_p2.py
"""


class AvgList(list):
    """child class of python's list class that can compute its average value
    """

    def computeAvg(self):
        """method that computes the average

        Raises:
            ValueError: raised if the list contains non-numerical values

        Returns:
            float: average value of the list
        """
        sm = 0  # init a sum counter
        for i in self:
            if isinstance(i, int) or isinstance(i, float):
                sm += i  # add to sum element if is numerical
            else:
                raise ValueError()  # else raise value error
        return sm / len(self)  # return average value


a = AvgList([1, 2, 3, 4])

print(a.computeAvg())
