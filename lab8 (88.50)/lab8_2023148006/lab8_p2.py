def removeValuesInPlace(L, threshold):
    """removes values above thresehold in L

    Args:
        L (list): list to be mutated
        threshold (int): threshold

    Returns:
        list: mutated list
    """
    i = 0
    while i < len(L):  # iterate
        if L[i] > threshold:  # if condition
            del L[i]  # remove
            i -= 1  # dont skip!!
        i += 1  # increment
    return L
