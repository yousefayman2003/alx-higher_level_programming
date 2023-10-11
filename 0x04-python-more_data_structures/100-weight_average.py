#!/usr/bin/python3
def weight_average(my_list=[]):
    total_weight = 0
    sum_ = 0
    for score, weight in my_list:
        total_weight += weight
        sum_ += score * weight

    return sum_ / total_weight
