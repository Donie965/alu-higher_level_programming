#!/bin/bash
# This script takes in a URL and displays the size of the response body in bytes.

# Check if URL argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Use curl to fetch the response body and get the size in bytes
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
