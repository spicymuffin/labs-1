import stack

operators = ['+', '-', '*', '/', '=']  # allowed operators
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # digits


def check_int(s):
    """checks wether string is composed of digits

    Args:
        s (str): string to check

    Returns:
        bool: result
    """
    fl = True
    for i in s:
        if i not in digits:  # iterate through s
            fl = False
            break
    return fl


def check_inp(a):
    """determines whether input is operator or an operand or nothing

    Args:
        a (str): input (could be a anything really)

    Returns:
        str: result
    """
    # this is literally it bc we can assume inputs are all ints or one of the allowed operators and they are separated by spaces
    if a in operators:
        return "operator"
    elif check_int(a):
        return "operand"
    else:
        return "nothing"


def exec_operator(a, b, op):
    """exec operator op using a and b

    Args:
        a (float or int): parameter 1
        b (float or int): parameter 2
        op (str): operator

    Returns:
        float or int: result of execution
    """
    if op == '+':  # this is pretty self explanatory
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b


# get input
inp = input("Enter an RPN expression: ").split(' ')

# main loop
while check_inp(inp[0]) != "nothing":
    # define a buch of stuff that gets used later
    s = stack.getStack()  # stack
    res = 0  # result
    malformed = False  # malformation (is this even a word lol) flag

    # if last input isn't a "=" or there are multiple "="s throw Evaluation error and exit
    if (not (inp[-1] == '=' and inp.count('=') == 1)):
        malformed = True

    if not malformed:
        # iterate through inputs
        for i in range(len(inp)):
            # determine type of input
            t = check_inp(inp[i])
            if t == "operator":  # if is an operator
                if inp[i] == '=':  # if "=" encountered it means we are at the end
                    res = stack.pop(s)
                    if res is None:  # if result None for some reason
                        malformed = True  # malformed idc
                    break

                o_d2 = stack.pop(s)  # get operand 2 from stack
                o_d1 = stack.pop(s)  # get operand 1 from stack

                # if division by zero malformed
                if o_d2 == 0 and inp[i] == '/':
                    malformed = True
                    break

                # if one of operands doesn't exist stack underflow -> malformed
                if o_d1 is None or o_d2 is None:
                    malformed = True
                    break

                # execute operator on the two operands
                r = exec_operator(o_d1, o_d2, inp[i])

                # push resulting operand to stack
                stack.push(s, r)

            if t == "operand":  # if is an operand
                stack.push(s, int(inp[i]))  # conver to int and push

    # if stack not empty its malformed
    if not stack.isEmpty(s):
        malformed = True

    # if malformed throw Evaluation error and exit
    if malformed:
        print("Evaluation error")
    else:
        # print result
        print(
            f"Value of expression: {int(res) if float.is_integer(float(res)) else format(res, '.2f')}")

    # get raw RPN expression, split it by spaces
    inp = input("Enter an RPN expression: ").split(' ')
