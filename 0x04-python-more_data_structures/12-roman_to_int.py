#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
              'C': 100, 'D': 500, 'M': 1000}
    number = 0
    n = len(roman_string)

    for i, letter in enumerate(roman_string):
        if i + 1 < n and romans[letter] < romans[roman_string[i+1]]:
            number -= romans[letter]
        else:
            number += romans[letter]

    return number
