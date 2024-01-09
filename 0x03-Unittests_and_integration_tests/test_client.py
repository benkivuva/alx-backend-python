#!/usr/bin/env python3
""" This project module contains the first unit test
for client.py file.
"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
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

    def test_public_repos_url(self):
        """ Tests that _public_repos_url returns a known payload.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            mock.return_value = {'repos_url': 'http://testing.url'}
            tg = GithubOrgClient('xyz')
            r = tg._public_repos_url
            self.assertEqual(r, mock.return_value.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """ Tests that test_public_repos returns a known payload.
        """
        get_json_mock.return_value = [
            {'name': 'repo_0'},
            {'name': 'repo_1'},
            {'name': 'repo_2'}
        ]
        get_json_mock()
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock:
            mock.return_value = [
                {'name': 'repo_0'},
                {'name': 'repo_1'},
                {'name': 'repo_2'}
            ]
            ghc = GithubOrgClient('xyz')
            r = ghc._public_repos_url
            self.assertEqual(r, mock.return_value)
            mock.assert_called_once()
            get_json_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """ Tests that has_license returns the correct values.
        """
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key),
            expected_result
        )


if __name__ == "__main__":
    unittest.main()
