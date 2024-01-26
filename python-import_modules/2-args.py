#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    nbArgs = len(args)

    if nbArgs == 0:
        print("{} arguments.".format(nbArgs), end="\n")
    elif nbArgs == 1:
        print("{} argument:".format(nbArgs), end="\n")
    elif nbArgs > 1:
        print("{} arguments:".format(nbArgs), end="\n")

    for index, value in enumerate(args, 1):
        print("{}: {}".format(index, value))
