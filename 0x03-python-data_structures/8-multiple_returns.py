#!/usr/bin/python3

def multiple_returns(sentence):
    len_ = len(sentence)
    if sentence == 0:
        first = None
    else:
        first = sentence[0]

    return len_, first
