def copyFiles(f1, f2, f3):
    """Copies file at paths f1 and f2 into a file at path f3 sequentially.

    Args:
        f1 (str): file 1 path
        f2 (str): file 2 path
        f3 (str): file 3 path

    Returns:
        int: operation result (0 for success, -1 for OSError)
    """
    # open output file
    try:
        out_file = open(f3, "w")
    except OSError:  # return -1 if can't be opened
        return -1

    # open input file 1
    try:
        inp_file_1 = open(f1, "r")
    except OSError:  # return -1 if can't be opened
        return -1

    for line in inp_file_1:
        out_file.write(line)
    inp_file_1.close()

    # open input file 2
    try:
        inp_file_2 = open(f2, "r")
    except OSError:  # return -1 if can't be opened
        return -1

    for line in inp_file_2:
        out_file.write(line)
    inp_file_2.close()

    # close output file
    out_file.close()

    return 0  # return 0 idk why
