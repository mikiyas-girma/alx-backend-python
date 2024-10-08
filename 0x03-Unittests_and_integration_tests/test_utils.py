#!/usr/bin/env python3
""" Tests for utils module. """
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests: the class that tests the access_nested_map method.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """
        Test the access_nested_map method.
        Args:
            nested_map (Dict)
            path (List, tuple, set)
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        Test the access_nested_map method exception return value
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Tests: the class that tests get_json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get_requests):
        """
        Test the get_json method to ensure it returns the expected output.
        Args:
            url: url to send http request to
            payload: expected json response
        """
        mock_get_requests.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get_requests.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Tests: the class that tests memoize method
    """

    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method):
        """
        a method to test memoize decorator function
        """
        obj = self.TestClass()
        result1 = obj.a_property
        result2 = obj.a_property

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)

        mock_a_method.assert_called_once()
