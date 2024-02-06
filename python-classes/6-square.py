#!/usr/bin/python3

"""class Square that defines a square"""


class Square:

    """ Square class that define a square with its size"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        else:
            self.__size = value

    @property  # getter
    def position(self):
        """method that returns the current square position"""
        return self.__position

    @position.setter  # setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
