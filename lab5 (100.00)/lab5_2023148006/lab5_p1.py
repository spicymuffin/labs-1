# input
inp = float(input("Enter a number: "))
# set max to -1 as a makeshift "flag"
mmax = -1
# if input is negative skip
while inp > 0:
    # update mmax with input variable ONLY if current input is bigger than mmax
    if mmax < inp:
        mmax = inp
    inp = float(input("Enter a number: "))

# if mmax = -1 then it means that no positive numbers were inputted so print.. yeah
if mmax == -1:
    print("No positive number was entered")
else:  # else print mmax which is the biggest positive number inputted
    print(f"The largest number entered was {format(mmax, '.2f')}")
