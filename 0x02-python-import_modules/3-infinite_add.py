#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    sum_ = 0

    for i in range(1, len(argv)):
        sum_ += int(argv[i])

    print("{:d}".format(sum_))
