#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        asci = ord(letter)
        flag = True if 97 <= asci <= 122 else False
        sub = 32 if flag else 0

        print(f"{ord(letter) - sub:c}", end="")
    print()
