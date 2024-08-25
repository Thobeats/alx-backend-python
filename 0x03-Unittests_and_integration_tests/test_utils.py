#!/usr/bin/env python3
"""Test Utils
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
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

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nestedMap, path, expected):
        with self.assertRaises(KeyError) as context:
            utils.access_nested_map(nestedMap, path)
        self.assertTrue(f"{expected}" in repr(context.exception))


class TestGetJson(unittest.TestCase):
    """Test the get_json from utils"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests):
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_requests.return_value = mock_response
        result = utils.get_json(test_url)

        mock_requests.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
