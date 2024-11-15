#!/usr/bin/python3
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
import os

def main():
    filename = "add_item.json"

    # Load existing items from the file if it exists
    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    # Add command line arguments to the list (excluding the script name)
    items.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()
