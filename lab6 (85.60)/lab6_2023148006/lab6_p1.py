# input
inp = input("Enter a first and last name: ")
# split it
spl = inp.split(' ')

# bounds vars
name_st = 0
name_ed = 0
surn_st = 0
surn_ed = 0
i = 0

# iterate through blanks
while i < len(inp) and inp[i] == " ":
    i += 1
name_st = i

# iterate through non-blanks
while i < len(inp) and inp[i] != " ":
    i += 1
name_ed = i + 1

# iterate through blanks
while i < len(inp) and inp[i] == " ":
    i += 1
surn_st = i

# iterate through non-blanks
while i < len(inp) and inp[i] != " ":
    i += 1
surn_ed = i

# print slices, defined by bound vars
print(f"{inp[surn_st:surn_ed]}, {inp[name_st]}.")
