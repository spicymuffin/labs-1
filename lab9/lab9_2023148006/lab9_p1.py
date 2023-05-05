import stack

inp = input("Enter parentheses and/or braces: ")

s = stack.getStack()

flag = True

for i in inp:
    if i == '(' or i == '{':
        stack.push(s, i)
    elif stack.isEmpty(s):
        flag = False
        break
    else:
        l = stack.pop(s)
        if l == '(' and i != ')':
            flag = False
            break
        if l == '{' and i != '}':
            flag = False
            break

if not stack.isEmpty(s):
    flag = False

if flag:
    print("Nested properly.")
else:
    print("Not properly nested.")
