#!/usr/bin/python3
def multiple_returns(sentence):
    len_ = len(sentence)
    return (len_, None) if len_ == 0 else (len_, sentence[0])
