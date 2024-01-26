#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = len(sys.argv)
    if args == 2:
        print("{} argument:".format(args - 1), end="\n")
    else:
        print("{} arguments:".format(args - 1), end="\n")

    for index in range(1, args):
        print("{}: ".format(index), sys.argv[index])
