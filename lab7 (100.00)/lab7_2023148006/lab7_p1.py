def zeroCheck(n1, n2, n3):
    """returns whether any of the integers is 0

    Args:
        n1 (int): integer 1
        n2 (int): integer 2
        n3 (int): integer 3

    Returns:
        bool: if zeros found true otherwise false
    """
    if n1 == 0 or n2 == 0 or n3 == 0:  # if all numbers are equal
        return True  # return true
    else:
        return False  # return false
