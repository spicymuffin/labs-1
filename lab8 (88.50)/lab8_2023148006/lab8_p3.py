def resetValues(L, threshold):
    """sets values above thresehold in a copy of L to 0

    Args:
        L (list): list to be used
        threshold (int): threshold

    Returns:
        list: modified copy of L
    """
    Result = []
    for i in range(len(L)):  # iterate
        if L[i] > threshold:  # if condition
            Result.append(0)  # to zero
        else:
            Result.append(L[i])
    return Result
