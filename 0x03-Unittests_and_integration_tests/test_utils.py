#!/usr/bin/env python3
"""
Python unit tests.
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.testCase):
    """Test Access nested map with key path."""
    @parameterized.expand([
        ("simple_map",{"a": 1}, ("a"),(1)),
        ("nested_map",{"a": {"b": 2}}, ("a"), ({"b": 2})),
        ("nested_map_access",{"a": {"b": 2}}, ("a", "b"), ({"b": 2},2))
    ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        """test_access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected, name)
    
    @parameterized.expand([
        ("simple_map",{}, ("a")),
        ("nested_map",{"a": 1}, ("a", "b"))
    ])
    def test_access_nestest_access_nested_map_exceptionted_map(self, name, nested_map, path, expected):
        """test_access_nested_map"""
        self.assertRaises(access_nested_map(nested_map,path), KeyError, name)