#!/usr/bin/python3
for alphabet in range(122, 96, -1):
    if abs(alphabet) % 2 != 0:
        alphabet = alphabet - 32
    print("{}".format(chr(alphabet)), end="")
