dig = [0, 0, 0, 0]
dig[0] = input("Enter leftmost digit: ")
dig[1] = input("Enter the next digit: ")
dig[2] = input("Enter the next digit: ")
dig[3] = input("Enter the next digit: ")

#yeah, i could do summ = int("".join(dig), 2) but meh
dig = list(map(int, dig))
summ = 0
for i in range(4):
    summ += dig[-(i+1)]*(2**i)

print("The value is", summ)
