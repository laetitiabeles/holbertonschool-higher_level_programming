#!/usr/bin/python3
""" class Square that inherits from BaseGeometry """

BaseGeometry = __import__('9-rectangle').BaseGeometry


class Square(BaseGeometry):
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
