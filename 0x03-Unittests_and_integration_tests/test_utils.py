#!/usr/bin/env python3
"""
Python unit tests.
"""
import requests
from parameterized import parameterized
from typing import Tuple, Dict, Any
import unittest
from unittest.mock import patch
from utils import (access_nested_map, get_json, memoize)


class TestAccessNestedMap(unittest.TestCase):
    """Test Access nested map with key path."""
    @parameterized.expand([
        ("simple_map",{"a": 1}, ("a"),(1)),
        ("nested_map",{"a": {"b": 2}}, ("a"), ({"b": 2})),
        ("nested_map_access",{"a": {"b": 2}}, ("a", "b"), (2))
    ])
    def test_access_nested_map(self, name: str, nested_map: Dict[str, Any],
                               path: Tuple[str, ...], expected: Tuple[Any, ...]
                               ) -> None:
        """test_access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    @parameterized.expand([
        ("simple_map",{}, ("a")),
        ("nested_map",{"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, name: str,
                                         nested_map: Dict[str, Any],
                                         path: Tuple[str, ...]) -> None:
        """test_access_nested_map"""
        with self.assertRaises(KeyError, msg=name) as e:
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """Test get json by mocking requists"""

    @parameterized.expand([
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url: str, test_payload: Dict[str, Any]) -> None:
        """test get json"""
        config: Dict[str, Any] = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()
