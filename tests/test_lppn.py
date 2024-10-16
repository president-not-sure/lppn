#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import lppn
from unittest import mock


class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code
        # Fake python ftp download page
        with open("tests/test_lppn_mock_content.txt", "rb") as file:
            self.content = file.read()

    def status_code(self):
        return self.status_code

    def content(self):
        return self.content

    def close(self):
        pass


class TestLppnGetMethod(unittest.TestCase):
    def setUp(self):
        # known and valid major number
        self.major = 3
        # known and valid minor number
        self.minor = 12
        # known and valid latest patch number
        self.latest_patch = 7

    @mock.patch("requests.sessions.Session.get")
    def test_valid_str_input(self, mock_session_get):
        mock.return_value = MockResponse(200)
        try:
            patch = lppn.get(str(self.major), str(self.minor))
        except:
            self.fail(
                f"'lppn.get({self.major}, {self.minor})' "
                "failed with valid inputs"
            )

        mock_session_get.assert_called_once()
        self.assertIsInstance(type(patch), type(int))
        self.assertEqual(patch, self.latest_patch)

    @mock.patch("requests.sessions.Session.get")
    def test_valid_int_input(self, mock_session_get):
        mock.return_value = MockResponse(200)
        try:
            patch = lppn.get(self.major, self.minor)
        except:
            self.fail(
                "'lppn.get({self.major}, {self.minor})'"
                "failed with valid inputs"
            )

        mock_session_get.assert_called_once()
        self.assertIsInstance(type(patch), type(int))
        self.assertEqual(patch, self.latest_patch)

    @mock.patch("requests.sessions.Session.get")
    def test_invalid_input_type(self, mock_session_get):
        mock.return_value = MockResponse(200)
        with self.assertRaises(TypeError):
            patch = lppn.get()
        with self.assertRaises(TypeError):
            patch = lppn.get("abc", "def")
        with self.assertRaises(TypeError):
            patch = lppn.get(3.1415, 2.71828)
        mock_session_get.assert_not_called()

    @mock.patch("requests.sessions.Session.get")
    def test_invalid_input_value(self, mock_session_get):
        mock.return_value = MockResponse(200)
        with self.assertRaises(ValueError):
            patch = lppn.get(-self.major, -self.minor)
        mock_session_get.assert_not_called()

    @mock.patch("requests.sessions.Session.get")
    def test_invalid_input_not_found(self, mock_session_get):
        mock.return_value = MockResponse(200)
        with self.assertRaises(RuntimeError):
            patch = lppn.get(1000000, 2000000)
        mock_session_get.assert_called_once()

    @mock.patch("requests.sessions.Session.get")
    def test_connection_error(self, mock_session_get):
        mock.return_value = MockResponse(404)
        with self.assertRaises(ConnectionError):
            patch = lppn.get(self.major, self.minor)
        mock_session_get.assert_called_once()


if __name__ == "__main__":
    unittest.main()
