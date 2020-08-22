#!/usr/bin/env python3
import glob, os, readline


def get_directory(text, state):
    trailing = ""
    if "~" in text:
        text = os.path.expanduser("~")  # Go to user's home directory
    if os.path.isdir((glob.glob(text + "*"))[state]):
        trailing = "/"  # Add a trailing slash if current location is a directory
    return (glob.glob(text + "*"))[state] + trailing


if __name__ == "__main__":
    readline.set_completer_delims(" \t\n;")  # Override default delimiters
    readline.parse_and_bind("tab: complete")
    readline.set_completer(get_directory)
    print(f"\n\U0001F4CD PWD is {os.getcwd()}/")
    input("\n\U0001F4C1 Please choose a root dir. for your project:  ")
