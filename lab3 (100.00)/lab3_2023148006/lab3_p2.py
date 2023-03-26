EAN = input("Enter the first 12 digits of an EAN: ")
# solvable with list(map(int, list(EAN))) but i guess we didnt learn that yet?
EAN = int(EAN)
d12 = EAN % 10
EAN //= 10
d11 = EAN % 10
EAN //= 10
d10 = EAN % 10
EAN //= 10
d9 = EAN % 10
EAN //= 10
d8 = EAN % 10
EAN //= 10
d7 = EAN % 10
EAN //= 10
d6 = EAN % 10
EAN //= 10
d5 = EAN % 10
EAN //= 10
d4 = EAN % 10
EAN //= 10
d3 = EAN % 10
EAN //= 10
d2 = EAN % 10
EAN //= 10
d1 = EAN % 10
EAN //= 10

# calculating EAC check digit
sm1 = d2 + d4 + d6 + d8 + d10 + d12
sm2 = d1 + d3 + d5 + d7 + d9 + d11
sm1 *= 3
sm1 += sm2
sm1 -= 1
sm1 %= 10
sm1 = 9 - sm1
# output
print("Check digit:", sm1)
