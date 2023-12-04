#!/usr/bin/python3
"""check if the object is an instance of a class that inherited"""

def inherits_from(obj, a_class):
    
    """ If obj is an inherited instance of a_class - True.
        Otherwise - False."""
    
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
