#!/usr/bin/python3
"""
A script that retrieves the GitHub user ID based on the provided credentials.

The script uses basic authentication with a GitHub username and personal access token.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

def get_github_user_id(username, token):
    """
    Retrieve the GitHub user ID using the provided username and personal access token.

    Args:
        username (str): The GitHub username.
        token (str): The GitHub personal access token (PAT).

    Returns:
        int: The GitHub user ID if the credentials are valid, or None if invalid.
    """
    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(username=username, password=token)
    
    try:
        # Make the GET request to GitHub API
        response = requests.get(url, auth=auth)

        # If the request was successful, return the user ID
        if response.status_code == 200:
            result = response.json()
            return result.get('id')
        else:
            # Handle errors like incorrect credentials or API issues
            print(f"Error {response.status_code}: {response.json().get('message', '')}")
            return None

    except requests.exceptions.RequestException as e:
        # Handle connection errors or timeout issues
        print(f"Request failed: {e}")
        return None


def main():
    """
    Main function to handle user input and display the result.
    
    Expects two command-line arguments: GitHub username and personal access token.
    """
    # Ensure there are exactly two arguments (username and token)
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    # Retrieve the user ID
    user_id = get_github_user_id(username, token)

    # Output the result (either user ID or None if credentials were invalid)
    if user_id:
        print(user_id)
    else:
        print("None")


if __name__ == '__main__':
    main()
