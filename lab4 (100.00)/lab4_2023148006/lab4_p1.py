# user input
t_i = int(input("Enter the taxable income in USD: "))

# main logic, realized with ifs and elifs
tax = -1
if t_i <= 750:
    tax = t_i * 0.02
elif t_i <= 2250:
    # subtract 750 from income to tax "amount over $750", calc 4% of that
    tax = 7.50 + (t_i - 750) * 0.04
elif t_i <= 3750:
    tax = 37.50 + (t_i - 2250) * 0.06
elif t_i <= 5250:
    tax = 82.50 + (t_i - 3750) * 0.08
elif t_i <= 7000:
    tax = 142.50 + (t_i - 5250) * 0.10
else:
    tax = 230.00 + (t_i - 7000) * 0.12

# print answer with the tax we calcualted
print(f"Tax due: {format(tax, '.2f')} USD")
