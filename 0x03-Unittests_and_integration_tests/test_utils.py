#!/usr/bin/env python3
""" Tests for utils module. """
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence
from utils import access_nested_map


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
