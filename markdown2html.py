#!/usr/bin/python3
"""A script to convert a Markdown file to HTML."""

import sys
import os

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) < 3:
        print(
            "Usage: ./markdown2html.py README.md README.html", file=sys.stderr
        )
        sys.exit(1)

    # Get the input and output file names
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    # Read the Markdown file
    try:
        with open(markdown_file, 'r') as md_file:
            markdown_content = md_file.read()
    except Exception as e:
        print(f"Error reading {markdown_file}: {e}", file=sys.stderr)
        sys.exit(1)

    # Convert Markdown content to HTML (basic conversion)
    html_content = markdown_content.replace('\n', '<br>\n')

    # Write the HTML content to the output file
    try:
        with open(html_file, 'w') as html_output:
            html_output.write(html_content)
    except Exception as e:
        print(f"Error writing to {html_file}: {e}", file=sys.stderr)
        sys.exit(1)

    # Exit with success
    sys.exit(0)
