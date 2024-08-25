#!/usr/bin/env python3
"""Test Utils
"""
import unittest
from parameterized import parameterized, parameterized_class
utils = __import__('utils')


class TestAccessNestedMap(unittest.TestCase):
    """Test Access Nested Map Class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nestedMap, path, expected):
        self.assertEqual(utils.access_nested_map(nestedMap, path), expected)


if __name__ == '__main__':
    unittest.main()
