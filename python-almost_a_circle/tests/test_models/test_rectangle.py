#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from tests.test_models.test_base import testBase

""" Create a test class for the rectangle class """


class testRectangle(testBase):
    """ Testing rectangle """

    @unittest.skip("Test non pertinent")
    def test_no_id(self):
        pass

if __name__ == '__main__':
    unittest.main()
