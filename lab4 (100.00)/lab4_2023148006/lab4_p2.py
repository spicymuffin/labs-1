# initiate some variables
i = -1
pos = 0
neg = 0
while i != 0:  # if input is zero exit loop, print
    i = int(input("Your number: "))
    # check number sign, increment corresponding counter
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1

# print counters
print(f"Positive values: {pos}")
print(f"Negative values: {neg}")
