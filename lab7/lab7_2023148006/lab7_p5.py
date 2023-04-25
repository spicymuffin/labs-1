isbn = input("Enter an ISBN: ") # get input
spl = isbn.split("-") # split

# print a bunch of stuff, mind the field-width
print(format(spl[0], ".<20") + "GS1 prefix")
print(format(spl[1], ".<20") + "Group identifier")
print(format(spl[2], ".<20") + "Publisher code")
print(format(spl[3], ".<20") + "Item number")
print(format(spl[4], ".<20") + "Check digit")