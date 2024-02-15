#!/usr/bin/python3
""" class Square that inherits from BaseGeometry """

BaseGeometry = __import__('9-rectangle').Rectangle


class Square(BaseGeometry):
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
