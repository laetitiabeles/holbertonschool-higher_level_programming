#!/usr/bin/python3
"""
class with method that print sorted list
"""


class MyList(list):
    """
    class that print sorted list

    Args:
        list (list): list to sorted
    """
    def print_sorted(self):
        """
        print sorted list
        """
        print(sorted(self))
