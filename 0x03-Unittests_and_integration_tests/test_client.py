#!/usr/bin/env python3
""" This project module contains the first unit test
for client.py file.
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient, get_json
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient inherits from unittest. TestCase to test
    client.GithubOrgClient.
    """
    @parameterized.expand([
        ("google", {}),
        ("abc", {})
    ])
    @patch('client.get_json')
    def test_org(self, url, expected_result, mock):
        """ Tests that GithubOrgClient.org returns the correct value.
        """
        mock.return_value = {}
        r = GithubOrgClient(url)
        self.assertEqual(r.org, expected_result)
        mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
