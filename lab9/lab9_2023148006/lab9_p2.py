import stack

inp = input("Enter an RPN expression: ").split(' ')

s = stack.getStack()
res = 0
operators = ['+', '-', '*', '/', '=']
malformed = False


def operator_or_operand(a):
    if a in operators:
        return "operator"
    return "operand"


def exec_operator(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b


if not (inp[-1] == '=' and inp.count('=') == 1):
    print("Evaluation error")
    exit()


for i in range(len(inp)):
    t = operator_or_operand(inp[i])
    if t == "operator":
        if inp[i] == '=':
            res = stack.pop(s)
            if res is None:
                malformed = True
            break

        o_d2 = stack.pop(s)
        o_d1 = stack.pop(s)

        if o_d2 == 0 and inp[i] == '/':
            malformed = True
            break

        if o_d1 is None or o_d2 is None:
            malformed = True
            break

        r = exec_operator(o_d1, o_d2, inp[i])

        stack.push(s, r)

    if t == "operand":
        stack.push(s, int(inp[i]))

if malformed:
    print("Evaluation error")
    exit()

print(f"Value of expression: {int (res) if float.is_integer(res) else format(res, '.2f')}")
