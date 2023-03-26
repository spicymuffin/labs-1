# i = 1 bc its displayed
r = 0
i = 1

# rows
while r <= 9:
    # index in row
    while i <= 10:
        # ex. row 2 index 2 gives us 2*10 + 2 (22)
        print(format(r*10 + i, ">3"), end="")
        i += 1 # increment index in row counter
    r += 1  # increment row counter
    i = 1  # reset index in row
    print()  # add newline

# idk why does it have to be two while loops so thats why this code
# is kinda weird :/
