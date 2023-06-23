"""
Name: Luigi Cussigh
Student ID: 2023148006
Lab problem: lab13_p7.py
"""

import os


def searchDir(directory, s):
    """
    Recursively searches 'directory' for .txt files
    that
    """

    files = os.listdir(directory)  # list directories
    return_list = []  # init return_list
    for file in files:
        fullname = directory + "/" + file  # fullname
        try:
            if os.path.isdir(fullname):
                # extend the return list
                # with newly found txt files if (any)
                return_list.extend(searchDir(fullname, s))
            else:
                if file[-3:] == "txt":
                    found = False
                    try:
                        file = open(fullname, "r")
                        lines = file.readlines()
                        for line in lines:
                            if line.find(s) != -1:
                                found = True  # set found flag
                                break

                        file.close()
                    except Exception:  # catch other exceptions idc
                        pass

                    # append to return_list if s in file
                    if found:
                        return_list.append(fullname)
        except OSError:
            # catch osError
            pass

    return return_list  # return list


# print((searchDir("C:/Users/luigi/Desktop/github/labs/lab13/doboggi_man", "gay")))
