def countLetters(line):
    """Count all letter characters in string ``line'' and write the
    result to file ``answer.txt''.

    Args:
        line (str): line to be processed
    """
    f = open("answer.txt", "w")  # open file for writing

    cnt = 0  # counter varaible
    for i in line:  # iterate through line
        if i.isalpha():  # if is a letter
            cnt += 1  # increment counter

    f.write(str(cnt) + '\n')  # write to file
    f.close()  # close file
