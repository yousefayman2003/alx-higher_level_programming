#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len_a, len_b = len(tuple_a), len(tuple_b)
    t1 = tuple_a[0] if len_a > 0 else 0
    t2 = tuple_a[1] if len_a > 1 else 0
    k1 = tuple_b[0] if len_b > 0 else 0
    k2 = tuple_b[1] if len_b > 1 else 0

    return t1 + k1, t2 + k2
