#!/usr/bin/env python3
""" This project module contains unit tests for utils.access_nested_map.
"""
from parameterized import parameterized
import unittest
from typing import Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap inherits from unittest.TestCase to test
    utils.access_nested_map.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected_result
    ):
        """ Method to test that the method returns what it is supposed to.
        """
        self.assertEqual(
            access_nested_map(nested_map, path), expected_result
        )

    @parameterized.expand([
        ({}, ("a",), KeyError, "Key not found: 'a'"),
        ({"a": 1}, ("a", "b"), KeyError, "Key not found: 'b'"),
    ])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence, expected_exception, expected_message
    ):
        """ Method to test that a KeyError is raised with the expected message.
        """
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)


if __name__ == '__main__':
    unittest.main()
