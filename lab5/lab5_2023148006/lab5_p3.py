# input
inp = int(input("Enter an integer: "))
lst = []
while inp != 0:
    # if value is OVER 100 append over
    if inp > 100:
        lst.append("over")
    # else just append the integer
    else:
        lst.append(inp)
    inp = int(input("Enter an integer: "))

# print the list
print(lst)
