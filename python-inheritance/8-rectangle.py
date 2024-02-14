#!/usr/bin/python3
""" class Rectangle that inherits from BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A representation of a rectangle"""
    def __init__(self, width, height):
        """init a rectangle
        Args:
        width (int): rectangle width
        height (int): rectangle height
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
