def evalPolynomial(x, L):
    """evaluate a polymnomial

    Args:
        x (int): polynomial input
        L (list): list containing coefficients

    Returns:
        int: result of evaluation
    """
    sm = 0
    for i in range(len(L)):
        sm += L[i]*x**i
    return sm