#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv
    n = len(argv)
    if n == 1:
        print("0 arguments.")
    elif n == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(n - 1))
        for i in range(1, n):
            print("{}: {}".format(i, argv[i]))
