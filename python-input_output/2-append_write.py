#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """Write a string to a text file (UTF8) and
    return the number of characters written."""
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
