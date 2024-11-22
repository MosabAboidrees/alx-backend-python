#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for access_nested_map function in utils module.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map with different inputs and outputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_output):
        """
        Test access_nested_map raises KeyError for invalid paths.
        """
        with self.assertRaises(expected_output) as context:
            access_nested_map(nested_map, path)
            # Assert that the exception message is correct
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test suite for get_json function in utils module.
    """

    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
    )
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json returns the expected output and makes an HTTP call.
        """
        # Create a Mock response object with a json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            # Call the function with the test URL
            result = get_json(test_url)

            # Assert that the function output matches the test payload
            self.assertEqual(result, test_payload)
