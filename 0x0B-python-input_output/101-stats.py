#!/usr/bin/python3
import sys

status_code = dict()
i = total_size = 0


def print_stats():
    """print the statistic"""
    print("File size: {total_size}".format(total_size))
    for key, value in sorted(status_code.items()):
        if value > 0:
            print("{:s}: {:d}".format(key, value))


try:
    for line in sys.stdin:
        lines = line.split()
        if len(lines) >= 2:
            stat = lines[-2]
            total_size += int(lines[-1])
            status_code[stat] = status_code.get(stat, 0) + 1
        i += 1

        if i % 10 == 0:
            print_stats()
    print_stats()
except KeyboardInterrupt as e:
    print_stats()
