#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer"""

    def test_DefaultArguments(self):
        """Test with default arguments"""
        self.assertIsNone(max_integer(), None)

    def test_TooManyArguments(self):
        """Test with extra arguments"""
        self.assertRaisesRegex(
        TypeError, " 0 to 1 positional arguments ", max_integer, [], [])

    def test_NonListArguments(self):
        """Test with non-iterable arguments"""
        self.assertRaises(TypeError, max_integer, 0)
        self.assertRaises(TypeError, max_integer, None)

    def test_EmptyListArguments(self):
        """Test with an empty list"""
        self.assertIs(max_integer([]), None)

    def test_BadListArguments(self):
        """Test with non-list or list-of-non-int iterable arguments"""
        self.assertEqual(max_integer('ABC'), 'C')
        self.assertEqual(max_integer([[], [0], [0, 0]]), [0, 0])
        self.assertRaises(TypeError, max_integer, [0, []])

    def test_MaximumInMiddle(self):
        """Test with the maximum value in the middle of the list"""
        self.assertEqual(max_integer([-1, 5, 2, 50, 3]), 50)
        self.assertEqual(max_integer([-10, -5, 0, 50, -1]), 50)

    def test_MaximumAtBeginning(self):
        """Test with the maximum value at the beginning of the list"""
        self.assertEqual(max_integer([50, -1, 5, 2, 3]), 50)
        self.assertEqual(max_integer([50, -10, -5, 0, -1]), 50)


