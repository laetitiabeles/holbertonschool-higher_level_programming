#!/usr/bin/python3
""" class Square that inherits from BaseGeometry """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define a square
    Args:
        Rectangle (Rectangle): mother class
    """
    def __init__(self, size):
        """init a square
        Args:
        size (int): square size
        """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """give square area
        Returns:
            int: square area
        """
        return self.__size ** 2

    def __str__(self):
        """print rectangle width and height
        Returns:
            str: rectangle
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
