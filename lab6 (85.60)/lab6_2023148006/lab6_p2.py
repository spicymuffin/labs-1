# digits
digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
# input
inp = input("Enter a fraction: ")
i = 0
# skip blanks
while inp[i] == ' ':
    i += 1

# found first arg. write it to n1
n1 = ""
while inp[i] in digits:
    n1 += inp[i]
    i += 1
n1 = int(str(n1))

# skip blanks
while inp[i] == ' ':
    i += 1

# skip slash
i += 1

# skip blanks
while inp[i] == ' ':
    i += 1

# found second arg. write it to n2
n2 = ""
while i < len(inp) and inp[i] in digits:
    n2 += inp[i]
    i += 1

# find gcd
n2 = int(str(n2))
mx = max(n1, n2)
mn = min(n1, n2)
while mx % mn != 0:
    mn = mx % mn
g = mn

# print output, omit /1 if denominator is 1.
print(f"In lowest terms: {n1//g}/{n2//g}" if n2 //
      g != 1 else f"In lowest terms: {n1//g}")
