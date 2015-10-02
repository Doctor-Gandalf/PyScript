#!/usr/local/bin/python3
# goto_gitpage.py - Launches a repo from my user profile in browser using an address from the
# command line or clipboard.

import webbrowser
import sys
import pyperclip
__author__ = 'Kellan Childers'

if len(sys.argv) > 1:
    # Get address from command line.
    repo = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    repo = pyperclip.paste()

webbrowser.open('https://www.github.com/Doctor-Gandalf/' + repo)

