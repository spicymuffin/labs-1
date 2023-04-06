# print banner
print("Currency Exchange Service")
print("\N{COPYRIGHT SIGN} 2022 Yonsei University")
print("\N{SMILING FACE WITH SMILING EYES} All rights reserved \N{SMILING FACE WITH SMILING EYES}")

# uuh summ variable
summ = 0
inp = float(input("Enter amount in dollars ($): "))
while inp != 0:
    # add to sum
    summ += inp
    inp = float(input("Enter amount in dollars ($): "))
# print sum multiplied by dollar exchange rate
print(f"Amount in Korean won (\N{WON SIGN}): {'{:,.2f}'.format(summ*1200)}")
