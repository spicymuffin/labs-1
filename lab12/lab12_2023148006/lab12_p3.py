"""
Name: Luigi Cussigh
Student ID: 2023148006
Lab problem: lab12_p3.py
"""
import random


def gen_permutation(n):
    """generate a random pemutation of a list comtaining 1 to n

    Args:
        n (int): length of list

    Returns:
        list: permutation
    """
    vals = list(range(0, n))
    out = []
    for i in range(n):
        # pick a random index
        pck = random.randint(0, len(vals) - 1)
        while vals[pck] == i:  # identity is not allowed
            pck = random.randint(0, len(vals) - 1)
            # swap places with random index bc if valueand index is equa;
            # and length is one that means that its a 9, so we need to swap
            # places with some value that went before the 9
            # we decide which one we will change with a value randomly
            # picked from the already generated output list
            if len(vals) == 1:
                pck = random.randint(0, len(out) - 1)
                tmp = out[pck]
                out[pck] = vals[0]
                vals[0] = tmp
                pck = 0
                break
        out.append(vals[pck])
        # the following 2 lines of code make this
        # function O(n) 😁
        vals[pck] = vals[-1]
        vals.pop()  # remove last elemrnt in choice set

    # return permutaiton
    return out


def gen_charset():
    """generates charset

    Returns:
        list: charset
    """
    # initialize charset
    charset = []

    # get some charcodes to generate a charset programmatically
    ord_a = ord("a")
    ord_z = ord("z")
    ord_A = ord("A")
    ord_Z = ord("Z")
    ord_0 = ord("0")
    ord_9 = ord("9")

    # cycle through charcodes, add to charset
    for i in range(ord_A, ord_Z + 1):
        charset.append(chr(i))

    for i in range(ord_a, ord_z + 1):
        charset.append(chr(i))

    for i in range(ord_0, ord_9 + 1):
        charset.append(chr(i))

    # dont forget whitespace
    charset.append(" ")

    # return charset
    return charset


def gen_decrypt_key(_encrypt_key):
    """generates a decryption key from an encryption key

    Args:
        _encrypt_key (dict): encrypt_key

    Returns:
        dict: decrypt_key
    """
    dct = dict()
    for i in _encrypt_key:  # reverse a dictionary basically
        dct[_encrypt_key[i]] = i
    return dct


def gen_encrypt_key(_charset, _permutation):
    """generates a encryption dictionary

    Args:
        _charset (list): charset
        _permutation (list): random non repeating integers in a list

    Returns:
        dict: encryption lookup dictionary
    """
    dct = dict()  # init empty dict
    for i in range(len(_charset)):  # iterate through kvps
        dct[_charset[i]] = _charset[
            _permutation[i]
        ]  # charset to permuatated mapping (encryption)

    return dct


def load_encrypt_key(_filename):
    """loads a encryption key into a dictionary
       from file with name _filename

    Args:
        _filename (str): filename (no extension)

    Returns:
        dict or int: key or operation result
    """
    key = dict()
    try:
        with open(_filename + ".key", "r") as file:
            for line in file:
                c_dec, c_enc = line[:-1].split(",")
                key[c_dec] = c_enc
    except Exception as ex:
        print(ex)
        return -1
    return key


def dump_encrypt_key(_filename, _key):
    """dumps a encryption key into file
       with name _filename from dictionary _key

    Args:
        _filename (str): filename (no extension)
        _key (dict): decrypt_key to dump

    Returns:
        int: operation result
    """
    try:
        with open(_filename + ".key", "w") as file:
            for c_dec in _key:
                c_enc = _key[c_dec]
                file.write(f"{c_dec},{c_enc}\n")
    except Exception as ex:
        print(ex)
        return -1
    return 0


filename = input("Enter a filename: ")
# filename = "test1.enc"

mode = ""
if filename[-3:] == "txt":
    mode = "enc"
elif filename[-3:] == "enc":
    mode = "dec"

filename_stripped = filename[:-4]

ext = ""
if mode == "enc":
    ext = ".enc"
elif mode == "dec":
    ext = ".txt"
else:
    print("invalid extension")
    exit(0)

try:
    file_inp = open(filename, "r")
    file_out = open(filename_stripped + ext, "w")
except Exception:
    print("error opening .txt or .enc file")

# encryption mode
if mode == "enc":
    # generaet charset
    charset = gen_charset()
    # generate permuation
    permutarion = gen_permutation(len(charset))

    # generate encrypt key
    encrypt_key = gen_encrypt_key(charset, permutarion)

    # dump decrypt key
    r = dump_encrypt_key("foo", encrypt_key)

    if r == -1:  # if exception caught in dump_decrypt_key
        print("error")
        exit(0)  # exit

    # iterate through input file
    for line in file_inp:
        out_line_lst = []
        for c in line:
            # do not encrypt newline characters
            if c == "\n":
                out_line_lst.append("\n")
            # do encrypt everything else based on on encrypt key
            else:
                out_line_lst.append(encrypt_key[c])

        # convert list to string and write
        out_line = "".join(out_line_lst)
        file_out.write(out_line)

# decryption mode
elif mode == "dec":
    # load decrypt key
    encrpt_key = load_encrypt_key("foo")
    decrypt_key = gen_decrypt_key(encrpt_key)

    if decrypt_key == -1:  # if exception caught in load_decrypt_key
        print("error")
        exit(0)  # exit

    for line in file_inp:
        out_line_lst = []
        for c in line:
            # do not decrypt newline characters
            if c == "\n":
                out_line_lst.append("\n")
            # do decrypt everything else based on on decrypt key
            else:
                out_line_lst.append(decrypt_key[c])

        # convert list to string and write
        out_line = "".join(out_line_lst)
        file_out.write(out_line)

# close files
file_inp.close()
file_out.close()
