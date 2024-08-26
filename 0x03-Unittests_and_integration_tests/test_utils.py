#!/usr/bin/env python3
"""
Python unit tests.
"""
from parameterized import parameterized
from typing import Tuple, Dict, Any
import unittest
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.testCase):
    """Test Access nested map with key path."""
    @parameterized.expand([
        ("simple_map",{"a": 1}, ("a"),(1)),
        ("nested_map",{"a": {"b": 2}}, ("a"), ({"b": 2})),
        ("nested_map_access",{"a": {"b": 2}}, ("a", "b"), ({"b": 2},2))
    ])
    def test_access_nested_map(self, name: str, nested_map: Dict[str, Any],
                               path: Tuple[str, ...], expected: Tuple[Any, ...]
                               ) -> None:
        """test_access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected, name)
    
    @parameterized.expand([
        ("simple_map",{}, ("a")),
        ("nested_map",{"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, name: str,
                                         nested_map: Dict[str, Any],
                                         path: Tuple[str, ...],
                                         expected: KeyError) -> None:
        """test_access_nested_map"""
        with self.assertRaises(KeyError, msg=name) as e:
            access_nested_map(nested_map,path)