"""
Name: Luigi Cussigh
Student ID: 2023148006
Lab problem: lab12_p2.py
"""


def moderateDays(mydict):
    """return a list containing days when temp was between 70 and 79

    Args:
        mydict (dict): dictionary containing temps

    Returns:
        list: resulting list
    """
    out = []
    for day in mydict:
        if 70 <= mydict[day] <= 79:  # self explanatory IMHO
            out.append(day)

    return out
