# input
n = int(input("Enter an integer: "))
# offset is how many characters we dont print at end of line
offset = 0
# n rows
for row in range(n):
    # n - row bc row = 0, we need to "invert" the index e.g. start from n
    # 2 * (n-row)-1 is the number of '*' that we have to print BUT that number
    # decreases by two every time so we compensate by adding offset
    for i in range((2*(n-row)-1)+offset):
        if i < offset:  # print offset amount of spaces basically ant then print stars
            print(' ', end='')
        else:
            print('*', end='')  # we dont need a newline
    # add newline after a row is complete
    print()
    # increment offset
    offset += 1
