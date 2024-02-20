#!/usr/bin/python3

import unittest
from tests.test_models.test_base import testBase
from models.rectangle import Rectangle
from models.base import Base

""" Create a test class for the rectangle class """


class testRectangle(testBase):
    """ Testing rectangle """

    @classmethod
    def setUpClass(cls):
        """ setUpClass """
        super().setUpClass()
        """ Crée une instance pour test_rectangle """
        test_instance = cls()
        """ Obtient le nom de la méthode """
        test_method_name = test_instance._testMethodName
        """ Obtient la valeur associée au nom sinon valeur = 0 """
        id_value = cls.id_values.get(test_method_name, 0)
        cls.rectangle_instance = Rectangle(1, 2, 3, 4, id_value)

    def test_rectangle_inherits_from_base(self):
        """ Testing inheritance """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_width(self):
        """Testing the Rectangle width getter"""
        self.assertEqual(self.rectangle_instance.width, 1)

    def test_height(self):
        """Testing the Rectangle height getter"""
        self.assertEqual(self.rectangle_instance.height, 2)

    def test_x(self):
        """Testing Rectangle x getter and setter"""
        self.rectangle_instance.x = 54
        self.assertEqual(self.rectangle_instance.x, 54)

    def test_y(self):
        """Testing Rectangle y getter and setter"""
        self.rectangle_instance.y = 45
        self.assertEqual(self.rectangle_instance.y, 45)

if __name__ == '__main__':
    unittest.main()
