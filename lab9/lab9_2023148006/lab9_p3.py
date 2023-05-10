# Palindrome Checker Program

# welcome
print('This program can determine if a given string is a palindrome\n')
print('(Enter return to exit)')

# init
empty_string = ''

# get string from user
chars = input('Enter string to check: ')

while chars != empty_string:
    if len(chars) == 1:
        print('A one letter word is by definition a palindrome\n')
    else:

        if chars[::-1].lower() == chars.lower(): # uhh palindrome is a reversed string?
            print(chars, 'is a palindrome\n')
        else:
            print(chars, 'is NOT a palindrome\n')

    # get next string from user
    chars = input('Enter string to check: ')
