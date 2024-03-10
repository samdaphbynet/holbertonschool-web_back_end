#!/usr/bin/env python3
"""
test access control
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize

from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    class to test access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        function to test access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """ Test method raises correct exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(unittest.TestCase):
    """
    class to test the get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, mock_get, test_payload):
        """
        Test function to test the get_json function
        """
        # Mock the behavior of requests.get
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Call the function requests
        with patch('requests.get', return_value=mock_response):
            r_response = get_json(mock_get)
            self.assertEqual(r_response, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        """ Tests memoize function """

        class TestClass:
            """ Test class """

            def a_method(self):
                """ Method to always return 42 """
                return 42

            @memoize
            def a_property(self):
                """ Returns memoized property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()
