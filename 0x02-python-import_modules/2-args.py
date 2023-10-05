#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv
    n = len(argv)
    if n == 1:
        print("0 arguments.")
    else:
        print("{} argument:".format(n))
        for i in range(1, n):
            print("{}: {}".format(i, argv[i]))
