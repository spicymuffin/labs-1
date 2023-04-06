# Temperature Conversion Program (Celsius-Fahrenheit / Fahrenheit-Celsius)

# Display program welcome
print('This program will convert temperatures (Fahrenheit/Celsius)')
print('Enter (F) to convert Fahrenheit to Celsius')
print('Enter (C) to convert Celsius to Fahrenheit')

# Get temperature to convert
which = input('Enter selection: ')

while which != 'F' and which != 'C':
    which = input("Please enter 'F' or 'C': ")

# inline if for tidiness, again
abs_zero = -273.15 if which == 'C' else -459.67

# we need to ask at least once
temp = int(input('Enter temperature to convert: '))
while temp <= abs_zero:
    # ask while we dont get something greater than absolute zero
    temp = int(input('Enter temperature to convert: '))

# `D`etermine temperature conversion needed and display results
if which == 'F':
    converted_temp = format((temp - 32) * 5/9, '.1f')
    print(temp, 'degrees Fahrenheit equals', converted_temp, 'degrees Celsius')
else:
    converted_temp = format((9/5 * temp) + 32, '.1f')
    print(temp, 'degrees Celsius equals', converted_temp, 'degrees Fahrenheit')
