#!/usr/bin/python3
""" Unittest for Rectangle class """

import unittest
import io
import sys


from tests.test_models.test_base import TestBase
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(TestBase):
    """ Testing Rectangle class """

    # SETUP + DEL
    def setUp(self):
        """ Init instance w/ width + height """
        self.rect = Rectangle(10, 20)

    def tearDown(self):
        """ Delete instance """
        del self.rect

    # INHERITANCE
    def test_rectangle_inherits_from_base(self):
        """ Testing inheritance """
        self.assertTrue(issubclass(Rectangle, Base))

    # Each attrs
    def test_width(self):
        """Testing the Rectangle width getter"""
        self.assertEqual(10, self.rect.width)

    def test_height(self):
        """Testing the Rectangle height getter"""
        self.assertEqual(20, self.rect.height)

    def test_x(self):
        """Testing Rectangle x getter and setter"""
        self.rect.x = 54
        self.assertEqual(54, self.rect.x)
        self.assertEqual(0, self.rect.y)

    def test_y(self):
        """Testing Rectangle y getter and setter"""
        self.rect.y = 45
        self.assertEqual(45, self.rect.y)
        self.assertEqual(0, self.rect.x)

    def test_rectangle_id(self):
        """Test the id for Rectangle"""
        rect = Rectangle(1, 3, 0, 0, 199)
        self.assertEqual(199, rect.id)

    # ATTRIBUTES
    def test_valid_attributes(self):
        """ Testing valid attributes """
        rect = Rectangle(10, 20, 5, 5)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 5)

    def test_invalid_width(self):
        """ Testing invalid width """
        with self.assertRaises(ValueError):
            Rectangle(0, 20, 5, 5)
        with self.assertRaises(ValueError):
            Rectangle(-10, 20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(None, 20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle("hello", 20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(True, 5)
        with self.assertRaises(TypeError):
            Rectangle([10, 6], 5)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)
        with self.assertRaises(TypeError):
            Rectangle(3.14, 5)

    def test_invalid_height(self):
        """ Testing invalid height """
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 5, 5)
        with self.assertRaises(ValueError):
            Rectangle(10, -20, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(10, None, 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(10, "hello", 5, 5)
        with self.assertRaises(TypeError):
            Rectangle(5, False)
        with self.assertRaises(TypeError):
            Rectangle(5, [10, 6])
        with self.assertRaises(ValueError):
            Rectangle(8, 0)
        with self.assertRaises(TypeError):
            Rectangle(5, 3.14)

    def test_invalid_x(self):
        """ Testing invalid x """
        with self.assertRaises(ValueError):
            Rectangle(10, 20, -5, 5)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, None, 5)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, "hello", 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 5, True)
        with self.assertRaises(TypeError):
            Rectangle(1, 5, [10, 6])
        with self.assertRaises(TypeError):
            Rectangle(5, 8, 3.14)

    def test_invalid_y(self):
        """ Testing invalid y """
        with self.assertRaises(ValueError):
            Rectangle(10, 20, 5, -5)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 5, None)
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 5, "hello")
        with self.assertRaises(TypeError):
            Rectangle(1, 5, 7, True)
        with self.assertRaises(TypeError):
            Rectangle(1, 5, 7, [10, 6])
        with self.assertRaises(TypeError):
            Rectangle(5, 5, 8, 3.14)

    def test_missing_height(self):
        """Expecting a type error because height and width are missing"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_missing_width(self):
        """Expecting an error because width is missing"""
        with self.assertRaises(TypeError):
            Rectangle(1)

if __name__ == '__main__':
    unittest.main()
