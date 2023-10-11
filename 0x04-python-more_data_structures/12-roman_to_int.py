#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    def convert_letter_to_num(letter):
        if letter == 'I':
            return 1
        elif letter == 'V':
            return 5
        elif letter == 'X':
            return 10
        elif letter == 'L':
            return 50
        elif letter == 'C':
            return 100
        elif letter == 'D':
            return 500
        elif letter == 'M':
            return 1000

    number = 0
    for letter in roman_string:
        number += convert_letter_to_num(letter)

    return number
