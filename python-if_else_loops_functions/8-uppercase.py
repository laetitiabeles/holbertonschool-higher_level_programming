#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            replace = ord(char) - (ord('a') - ord('A'))
            charUpper = chr(replace)
            print(charUpper, end="")
        else:
            print(char, end="")
    print()
