def resetValuesInPlace(L, threshold):
    """sets values above thresehold in L to 0

    Args:
        L (list): list to be mutated
        threshold (int): threshold

    Returns:
        list: mutated list
    """
    for i in range(len(L)):
        if L[i] > threshold:
            L[i] = 0
    return L
