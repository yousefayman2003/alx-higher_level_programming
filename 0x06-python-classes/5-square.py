#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        for i in range(self.size):
            for j in range(self.size):
                end = "\n" if j is self.size - 1 and i != j else ""
                print("#", end=end)
        print()
