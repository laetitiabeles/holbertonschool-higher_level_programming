#!/usr/bin/python3
def value(roman_numeral):
    if (roman_numeral == 'I'):
        return 1
    if (roman_numeral == 'V'):
        return 5
    if (roman_numeral == 'X'):
        return 10
    if (roman_numeral == 'L'):
        return 50
    if (roman_numeral == 'C'):
        return 100
    if (roman_numeral == 'D'):
        return 500
    if (roman_numeral == 'M'):
        return 1000
    return -1


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    else:
        result = 0
        idx = 0

        while (idx < len(roman_string)):
            symbol = value(roman_string[idx])
            if (idx + 1 < len(roman_string)):
                next_symbol = value(roman_string[idx + 1])
                if (symbol >= next_symbol):
                    result = result + symbol
                    idx = idx + 1
                else:
                    result = result + next_symbol - symbol
                    idx = idx + 2
            else:
                result = result + symbol
                idx = idx + 1
        return result
