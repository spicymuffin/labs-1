# delta between lowercase and uppercase
case_shift = ord('a') - ord('A')
# output list
output = []
inp = input("Enter a word (q to quit): ")
while inp != 'q':  # iterate through word
    i = 0
    inp_lower = ""  # lowercase input
    while i < len(inp):
        if 'A' <= inp[i] <= 'Z':  # if uppercase
            inp_lower += chr(ord(inp[i]) + case_shift)  # make lower
        else:
            inp_lower += inp[i]  # else just leave it
        i += 1

    # if the char appears in the word (except 1 char)
    if inp_lower[0] in inp_lower[1:]:
        output.append(inp)

    inp = input("Enter a word (q to quit): ")

output.sort()  # sort
print(output)  # output
