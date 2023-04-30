def lookAndSay(n, i):
    """checks wether cycle is in sequence

    Args:
        n (int): inital D
        i (int): sequence length
    Returns:
        bool: result
    """
    def calc_nxt(m):
        m = str(m)
        d = [0]*10  # empty list (index represents digit)
        for i in n:  # iterate number
            d[int(i)] += 1  # increment digit if found

        out = ""  # output
        for i in range(len(d)):
            if d[i] != 0:
                out += str(d[i])  # add count to output
                out += str(i)  # add digitr to output
        return ''.join(out)  # return str

    r = []  # holds sequence
    nxt = str(n)
    for j in range(i):
        print(f"{j+1}: {nxt}")  # print
        r.append(nxt)  # append to sequence list
        nxt = calc_nxt(nxt)  # calc next sequence member
    # if one occurrence or more in list then loop is detected i guess
    return r[-1] in r[:-1]
