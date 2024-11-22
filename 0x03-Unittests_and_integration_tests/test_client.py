#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test suite for GithubOrgClient class.
    """

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org_name, expected, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        # Set up mock return value
        mock_get_json.return_value = expected

        # Initialize the GithubOrgClient with the test organization name
        client = GithubOrgClient(org_name)

        # Call the .org property
        result = client.org

        # Assert that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        # Assert that the result matches the expected value
        self.assertEqual(result, expected)

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that GithubOrgClient._public_repos_url returns the correct URL.
        """
        # Define a mock payload
        mock_payload = {
            "repos_url": "https://api.github.com/orgs/test-org/repos"}
        mock_org.return_value = mock_payload

        # Initialize GithubOrgClient
        client = GithubOrgClient("test-org")

        # Call the _public_repos_url property
        result = client._public_repos_url

        # Assert that the result matches the mocked repos_url
        self.assertEqual(result, mock_payload["repos_url"])
