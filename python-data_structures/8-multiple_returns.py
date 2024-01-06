#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        lenofsen = len(sentence)
    else:
        lenofsen = 0
    return (lenofsen, sentence if not sentence else sentence[:1])
