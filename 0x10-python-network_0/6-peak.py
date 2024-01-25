#!/usr/bin/python3
"""
    A module containing `find_peak` function.
"""


def find_peak(nums):
    """
        Finds a peak in a list of unsorted integers.

        Args:
            nums (list): array of integers

        Returns:
            a peak if it's found, None otherwise
    """
    n = len(nums)

    if n > 1:
        if nums[0] > nums[1]:
            return nums[0]

        elif nums[-1] > nums[-2]:
            return nums[-1]

        prev = nums[0]
        cur = nums[1]

        for i in range(2, size):
            next_number = nums[i]
            
            if prev <= cur >= next_number:
                return cur
            
            prev = cur
            cur = next_number

    return nums[0] if n == 1 else None
