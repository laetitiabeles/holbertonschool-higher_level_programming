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

    def area(self):
        """give rectangle area
        Returns:
            int: rectangle area
        """
        return self.__width * self.__height

    def __str__(self):
        """print rectangle width and height
        Returns:
            str: rectangle
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
