#!/usr/bin/puthon3
"""contains the MyList class"""

class MyList(list) :
    """initializes the object"""
    def __init__(self):
        super.__init__()
    
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
