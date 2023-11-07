#!/usr/bin/python3
"""Module that contains the solution for task 9."""


class Student:
    """Student class"""

    def __init__(self, firstname, lastname, age):
        """Constructor"""
        self.first_name = firstname
        self.last_name = lastname
        self.age = age

    def to_json(self):
        """returns a dictionary representation of student"""
        return self.__dict__
