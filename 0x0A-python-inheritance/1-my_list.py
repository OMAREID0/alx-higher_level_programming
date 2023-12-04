#!/usr/bin/puthon3
"""contains the MyList class"""

class MyList(list) :
    """initializes the object"""
    
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
