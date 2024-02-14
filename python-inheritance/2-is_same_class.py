#!/usr/bin/python3
"""
check if object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    check if object is exactly an instance of the specified class

    Args:
        obj (object): object to check
        a_class (class): class to check

    Returns:
        bool: True if object is exactly an instance of the specified class
    """
    return type(obj) is a_class
