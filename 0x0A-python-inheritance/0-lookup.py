#!/usr/bin/python3
""" function that returns the list of available attributes and methods"""

def lookup(obj):
    """Return a list of an object's available attributes."""
    print(dir(obj))
