#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = len(sys.argv[1:])

    if args == 1:
        print("{} argument:".format(args), end="\n")
    elif args == 0:
        print("{} argument.".format(args), end="\n")
    elif args > 1:
        print("{} arguments:".format(args), end="\n")

    for index, value in enumerate(sys.argv[1:], 1):
        print("{}: {}".format(index, value))
