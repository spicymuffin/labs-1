def resetValuesInPlace(L, threshold):
    """sets values above thresehold in L to 0

    Args:
        L (list): list to be mutated
        threshold (int): threshold

    Returns:
        list: mutated list
    """
    for i in range(len(L)):
        if L[i] > threshold:  # if element bigger than threshold
            L[i] = 0  # set to zero
    return L
