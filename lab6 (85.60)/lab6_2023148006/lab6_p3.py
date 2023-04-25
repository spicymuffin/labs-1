# Password Encryption/Decryption Program

import sys

# init
password_out = ''
case_changer = ord('a') - ord('A')
encryption_key = (('a', 'm'), ('b', 'h'), ('c', 't'),
                  ('d', 'f'), ('e', 'g'), ('f', 'k'),
                  ('g', 'b'), ('h', 'p'), ('i', 'j'),
                  ('j', 'w'), ('k', 'e'), ('l', 'r'),
                  ('m', 'q'), ('n', 's'), ('o', 'l'),
                  ('p', 'n'), ('q', 'i'), ('r', 'u'),
                  ('s', 'o'), ('t', 'x'), ('u', 'z'),
                  ('v', 'y'), ('w', 'v'), ('x', 'd'),
                  ('y', 'c'), ('z', 'a'), ('#', '!'),  # add symbols to key
                  ('@', '('), ('%', ')'))

encrypting = True

# get password
password_in = input('Enter password: ')
digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
chrs = ('#', '@', '%')

# validity flags (?)
letter = False
digit = False
special = False
broken = False
for i in password_in:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:  # check whether char is A-Z or a-z
        letter = True
    elif i in digits:  # check whether char is a digit
        digit = True
    elif i == '#' or i == '@' or i == '%':  # check whether char is a special symbol
        special = True
    else:
        # if a symbol isnt defined the password is broken thus must be rejected
        broken = True
        break

# exit if pwd is broken
if not (letter and digit and special) or broken:
    print("Invalid password!")
    sys.exit(0)

# perform encryption / decryption
if encrypting:
    from_index = 0
    to_index = 1
else:
    from_index = 1
    to_index = 0

case_changer = ord('a') - ord('A')

for ch in password_in:
    letter_found = False

    # make sure the encryption code now recognizes special symbols by adding ch in chrs
    for t in encryption_key:
        if (('a' <= ch and ch <= 'z') or ch in chrs) and ch == t[from_index]:
            password_out = password_out + t[to_index]
            letter_found = True
        elif (('A' <= ch and ch <= 'Z') or ch in chrs) and chr(ord(ch) + 32) == t[from_index]:
            password_out = password_out + chr(ord(t[to_index]) - case_changer)
            letter_found = True

    if not letter_found:
        password_out = password_out + ch

# output
if encrypting:
    print('Your encrypted password is:', password_out)
else:
    print('Your decrypted password is:', password_out)
