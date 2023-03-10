# Temperature conversion program Celsius->Fahrenheit

# program greeting:
print('This program will convert degrees Celsius to degrees Fahrenheit')

# get temperature in Celsius:
c = float(input('Enter degrees Celsius: '))

# convert Fahrenheit to Celsius:
f = (c * 9 / 5) + 32

# print result:
print(c, 'degrees Celsius equals', format(f, '.1f'), 'degrees Fahrenheit')
