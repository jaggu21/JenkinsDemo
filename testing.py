#!/usr/bin/python3

import unittest

from program import *

class Test(unittest.TestCase):
    def addition_test(self):
        data = [5, 10]
        expected = 15
        self.assertEqual(addition(data[0], data[1]), expected)

    def subtraction_test(self):
        data = [5, 10]
        expected = -5
        self.assertEqual(subtraction(data[0], data[1]), expected)

    def multiplication_test(self):
        data = [5, 10]
        expected = 15
        self.assertEqual(multiplication(data[0], data[1]), expected)

    def division_test(self):
        data = [10, 2]
        expected = 5
        self.assertAlmostEqual(division(data[0], data[1]), expected)

if __name__ == '__main__':
    unittest.main()