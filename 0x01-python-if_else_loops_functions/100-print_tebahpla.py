#!/usr/bin/python3
for i in range(122, 96, -1):
    sub = 0 if i % 2 == 0 else 32
    print("{:c}".format(i - sub), end="")
