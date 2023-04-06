# input
inp = input("Enter a name (q to quit): ")

# alright use list
lst = []

cnt = 0
while inp != 'q':  # if input is q skip
    lst.append(inp)
    inp = input("Enter a name (q to quit): ")

for entry in lst:  # iterate through lst
    for char in entry:  # iterate through entry
        if char == 'a' or char == 'A':  # if char is a increment cnt
            cnt += 1

# print
print(f"Appearance of letter 'a': {cnt}")
