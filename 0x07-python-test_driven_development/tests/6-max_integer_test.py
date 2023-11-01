#!/usr/bin/python3
"""Unittests for max_integer(..)"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_max_int(unittest.TestCase):
    """Define unittests for max_integer(..)"""

    def test_empty_list(self):
        """Test empty list"""
        self.assertEqual(max_integer([]), None)

    def test_ordered_list(self):
        """Test an ordered list of int"""
        self.assertEqual(max_integer([7, 8, 9, 10]), 10)

    def test_notordered_list(self):
        """Test an not ordered list of integers."""
        self.assertEqual(max_integer([7, 12, 4, 10]), 12)

    def test_one_element_list(self):
        """Test list with one int"""
        self.assertEqual(max_integer([1]), 1)

    def test_list_with_same_max(self):
        """Test list with same max"""
        self.assertEqual(max_integer([80, 71, 80]), 80)

    def test_list_with_negative_max(self):
        """Test list of negative integers."""
        self.assertEqual(max_integer([-7, -5, -17]), -5)

    def test_list_with_tuple(self):
        """Test tuple of integers."""
        self.assertEqual(max_integer((7, 10, 12, 4)), 12)

    def test_list_with_empty_tuple(self):
        """Test an empty tuple"""
        self.assertEqual(max_integer(()), None)

    def test_list_with_empty_string(self):
        """Test an empy string"""
        self.assertEqual(max_integer(""), None)

    def test_list_with_string(self):
        """Test a string"""
        self.assertEqual(max_integer("Hey"), 'y')


if __name__ == "__main__":
    unittest.main()
