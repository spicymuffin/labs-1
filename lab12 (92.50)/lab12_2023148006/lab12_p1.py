"""
Name: Luigi Cussigh
Student ID: 2023148006
Lab problem: lab12_p1.py
"""


def addDailyTemp(mydict, day, temperature):
    """adds kvp day: temperature to dict mydict if key isnt present in mydict

    Args:
        mydict (dict): dictionary
        day (immutable,any): key
        temperature (any): value

    Returns:
        dict: resulting dictionary
    """
    if day not in mydict:  # if key not in mydict
        mydict[day] = temperature  # add

    return mydict  # return mydict
