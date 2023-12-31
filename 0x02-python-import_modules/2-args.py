#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    from sys import argv

    argc = int(len(argv)) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 arguments:")
    else:
        print("{} arguments:".format(argc))
    for i in range(argc):
        print("{}: {}".format(i + 1, argv[i + 1]))
