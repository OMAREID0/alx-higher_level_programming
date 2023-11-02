#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    
    counter = 0
    argc = len(argv) - 1
    
    for i in range(argc):
        argv[i + 1] = int(argv[i + 1])
        counter += argv[i + 1]
    print(counter)