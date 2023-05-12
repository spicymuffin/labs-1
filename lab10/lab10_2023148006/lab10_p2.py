def copyFiles(f1, f2, f3):
    """Copies file at paths f1 and f2 into a file at path f3 sequentially.

    Args:
        f1 (str): file 1 path
        f2 (str): file 2 path
        f3 (str): file 3 path
    """
    # open output file
    out_file = open(f3, "w")

    # write input file 1
    inp_file_1 = open(f1, "r")
    for line in inp_file_1:
        out_file.write(line)
    inp_file_1.close()

    # write input file 2
    inp_file_2 = open(f2, "r")
    for line in inp_file_2:
        out_file.write(line)
    inp_file_2.close()

    # close output file
    out_file.close()

    return 0  # return 0 idk why


copyFiles('in1.txt', 'in2.txt', 'out.txt')
