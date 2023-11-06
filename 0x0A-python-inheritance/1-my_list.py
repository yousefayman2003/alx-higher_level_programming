#!/usr/bin/python3
"""Module that contains MyList Class."""


class MyList(list):
    """My list Class"""

    def print_sorted(self):
        """Method for printing list in ascending order."""
        print(sorted(self))
