import stack

# get input
inp = input("Enter parentheses and/or braces: ")

# init stack
s = stack.getStack()

# success flag
flag = True

# iterate through input
for i in inp:
    # if opening brackets push to stack
    if i == '(' or i == '{':
        stack.push(s, i)
    # if a closing bracket is encountered but nothing is in the stack then
    # un-raise flag
    elif stack.isEmpty(s):
        flag = False
        break
    else:
        la = stack.pop(s)  # get last stashed bracket
        if la == '(' and i != ')':  # if brackets dont match un-raise flag
            flag = False
            break
        if la == '{' and i != '}':  # if brackets dont match un-raise flag
            flag = False
            break

# if stack not empty by the time all input is processed un-raise flag
if not stack.isEmpty(s):
    flag = False

if flag:  # raised flag meanscorrect nesting
    print("Nested properly.")
else:
    print("Not properly nested.")
