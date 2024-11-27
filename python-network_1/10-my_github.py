#!/usr/bin/python3
"""A script that takes GitHub credentials and returns the user ID."""

if __name__ == '__main__':
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    # Ensure there are enough arguments
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        sys.exit(1)

    url = 'https://api.github.com/user'
    user = sys.argv[1]
    token = sys.argv[2]  # This should be a personal access token (PAT)

    # Use token-based authentication instead of username/password
    auth = HTTPBasicAuth(username=user, password=token)

    try:
        response = requests.get(url, auth=auth)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            result = response.json()
            print(result.get('id'))
        else:
            # If the request failed, print the error message
            print("Invalid credentials or API request failed.")
            print(f"Error {response.status_code}: {response.json().get('message', '')}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
