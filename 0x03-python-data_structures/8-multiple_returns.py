#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    return (sentence[0] if length else None, length)
