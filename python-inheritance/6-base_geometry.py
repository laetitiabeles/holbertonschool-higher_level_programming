#!/usr/bin/python3
"""
class that return a raise exception
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def __init__(self, area):
        self.area = area

    def area(self):
        raise Exception("area() is not implemented")
