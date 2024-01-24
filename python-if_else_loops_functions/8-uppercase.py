#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            replace = ord(char) - (ord('a') - ord('A'))
            charUpper = chr(replace)
            result += charUpper
        else:
            result += char
    print(result)
