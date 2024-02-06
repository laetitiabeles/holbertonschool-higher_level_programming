#!/usr/bin/python3

"""class Square that defines a square"""


class Square:

    """ Square class that define a square with its size"""

    def __init__(self, size=0):
        self.__size = size

    @property  # getter
    def size(self):
        """method that returns the current square size"""
        return self.__size

    @size.setter  # setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """method that prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for index in range(self.__size):
                print("#" * self.__size)
