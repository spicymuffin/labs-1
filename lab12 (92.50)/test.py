# """
# Name: Luigi Cussigh
# Student ID: 2023148006
# Lab problem: lab12_p4.py
# """

# import random


# def gen_permutation(n):
#     """generate a random pemutation of a list comtaining 1 to n

#     Args:
#         n (int): length of list

#     Returns:
#         list: permutation
#     """
#     vals = list(range(0, n))
#     out = []
#     for i in range(n):
#         # pick a random index
#         pck = random.randint(0, len(vals) - 1)
#         while vals[pck] == i:  # identity is not allowed
#             pck = random.randint(0, len(vals) - 1)
#             if len(vals) == 1:
#                 pck = random.randint(0, len(out) - 1)
#                 tmp = out[pck]
#                 out[pck] = vals[0]
#                 vals[0] = tmp
#                 pck = 0
#                 break
#         out.append(vals[pck])
#         # the following 2 lines of code make this
#         # function O(n) 😁
#         vals[pck] = vals[-1]
#         vals.pop()  # remove last elemrnt in choice set

#     # return permutaiton
#     return out


# for j in range(10000):
#     a = gen_permutation(10)
#     for i in range(len(a)):
#         if a[i] == i:
#             print("U SUCK!")
#         for j in range(10):
#             if j not in a:
#                 print("U SUCK!")
#     print(a)


def find_gcd(a, b):
    """finds gcd of a and b

    Args:
        a (int): input 1
        b (int): input 2

    Returns:
        int: gcd
    """
    gcd = 0
    while a != 0 or b != 0:
        a = a % b
        if a == 0:
            gcd = b
            break
        b = b % a
        if b == 0:
            gcd = a
            break
    return gcd


print(find_gcd(10, 5))
