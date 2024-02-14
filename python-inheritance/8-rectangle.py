#!/usr/bin/python3
"""
class that return a raise exception
"""


class BaseGeometry:
    """
    class BaseGeometry
    """
    def __init__(self, width, height):
        """Initializes the `width` and `height` properties"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Raises an exception when you call this function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks a integer value
        Args:
            name (str): The name of the value.
            value (int): The value.
        Raises:
            TypeError: If `value` isn't a integer.
            ValueError: If `value` is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
