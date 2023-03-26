# get input
num = int(input("Enter a number: "))
tmp = num

# determine # of digits by dividing by 10 until we are left with a 0
cnt = 0
while num != 0:
    num //= 10
    cnt += 1

# inline if for tidiness
print(f"The number {tmp} contains {cnt} digit{'' if cnt == 1 else 's'}")
