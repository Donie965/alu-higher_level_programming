#!/usr/bin/python3
import sys
from 6-load_from_json_file import load_from_json_file
from 5-save_to_json_file import save_to_json_file

# Define the filename
filename = "add_item.json"

# Try to load the existing list from the file
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add command-line arguments to the list (ignoring the script name)
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)

import json

def save_to_json_file(my_obj, filename):
    """Save an object to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)

        import json

def load_from_json_file(filename):
    """Load an object from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)
