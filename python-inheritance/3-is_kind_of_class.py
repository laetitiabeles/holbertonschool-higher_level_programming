#!/usr/bin/python3
"""
check if object is an instance of, or if the object is an instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    check if object is an instance of, or if the object is an instance of a class that inherited from, the specified class

    Args:
        obj (object): object to check
        a_class (class): class to check

    Returns:
        bool: True if object is an instance of, or if the object is an instance of a class that inherited from, the specified class
    """
    return isinstance(obj, a_class)
