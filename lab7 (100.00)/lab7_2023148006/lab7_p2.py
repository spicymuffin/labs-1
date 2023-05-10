def ordered3(n1, n2, n3):
    """checks whether the input integers are in order from smallest to largest

    Args:
        n1 (int): integer 1
        n2 (int): integer 2
        n3 (int): integer 3

    Returns:
        _type_: true of the parameters are in order smallest to largest, otherwise false
    """
    if n1 <= n2 <= n3:  # if this is true
        return True  # return true
    else:
        return False  # return false
