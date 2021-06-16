#! python3
# mapit,py - launches a map in the browser using an address from the command line or clipboard.

import sys
import webbrowser
import pyperclip

if len(sys.argv) > 1:
    # Get address from the command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from the clipboard.
    address = pyperclip.paste()

webbrowser.open(f'https://www.google.com/maps/place/{address}')
