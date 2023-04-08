import math
# input
inp = input("Evaluate the equation: ")
# split by args
spl = inp.split(' ')
# args processing
func = spl[0]
arg = float(spl[1])
terms = int(spl[2])

# Taylor sequence sum
sm = 0
if func == "exp":  # change which formula we use depending on first arg
    for i in range(terms):
        sm += arg**i/math.factorial(i)
elif func == "cos":
    for i in range(terms):
        sm += ((-1)**i)/(math.factorial(2*i))*(arg**(2*i))
elif func == "sin":
    for i in range(terms):
        sm += ((-1)**i)/(math.factorial(2*i + 1))*(arg**(2*i + 1))
else:  # this code should never run provided the input isnt broken
    print("uh oh")

#print outpput as requested
print(
    f"Using {terms} term(s), {func}({format(arg, '.4f')}) is {format(sm, '.6f')}")
