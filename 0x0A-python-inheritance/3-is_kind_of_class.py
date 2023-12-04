#!/usr/bin/python3
"""check if object is an instance"""

def is_kind_of_class(obj, a_class):
    """return True if obj is instance or inherited instance of a_class"""
   
    if isinstance(obj, a_class):
        return (True)
    return (False)
