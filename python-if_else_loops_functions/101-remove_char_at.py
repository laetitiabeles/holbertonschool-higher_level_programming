#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str

    result = ""
    for index in range(n):
        result += str[index]

    for index in range(n + 1, len(str)):
        result += str[index]

    return result
