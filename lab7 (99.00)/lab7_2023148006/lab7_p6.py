def scalar_mult(y, A):
    """multiplies matrix by scalar

    Args:
        y (int): scalar
        A (two dimensional list): matrix

    Returns:
        two dimensional list: resulting matrix
    """
    B = A[:]  # copy matrix
    for i in range(len(B)):  # iterate outer list
        for j in range(len(B[i])):  # iterate sub list
            B[i][j] *= y  # multiply
    return B  # return value
