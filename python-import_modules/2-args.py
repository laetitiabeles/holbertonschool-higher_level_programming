#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    nbArgs = len(args)

    if nbArgs == 0:
        print("0 arguments.")
    elif nbArgs == 1:
        print("1 argument:")
        print("1: {}".format(args[0]))
    else:
        print("{} arguments:".format(nbArgs))

    for index, value in enumerate(args, 1):
        print("{}: {}".format(index, value))
