#!/usr/bin/puthon3
class MyList(list) :
    """initializes the object"""
    super.__init__()
    
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
