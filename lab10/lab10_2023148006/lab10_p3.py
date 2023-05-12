def countAllLetters(line):
    """Counts letters in 'line' and returns result list. If the line
    does not contain any letter, returns an empty list.

    Args:
        line (str): line to process

    Returns:
        list: letter count list (sorted)
    """

    offset = ord("a")  # offset for letter codes

    cnt_lst = [0] * 26  # counter list

    for c in line:  # iterate through input
        c = c.lower()  # "lower case-ify"
        if c.isalpha():  # if is a letter
            # increment counter list at offset index
            cnt_lst[ord(c) - offset] += 1

    ltr_lst = []  # final list
    for i in range(len(cnt_lst)):  # iteratet through conter list
        if cnt_lst[i] != 0:  # if letter occurences isn't 0
            # append to final list a tuple containing a letter code corresponding to offset index
            # and the count of that letter
            ltr_lst.append((chr(i + offset), cnt_lst[i]))

    return ltr_lst  # return final list
