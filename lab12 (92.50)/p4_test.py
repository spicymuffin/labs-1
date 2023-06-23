from lab12_p4 import Fraction

f1 = Fraction(2, 12)
f2 = Fraction(1, 6)
f2.num = 2
print("f1:", f1)  # f1: 1/6
print("f2:", f2)  # f2: 2/6
f2.reduce()
print("f2:", f2)  # f2: 1/3
f2.adjust(3)
print("f2:", f2)  # f2: 3/9
