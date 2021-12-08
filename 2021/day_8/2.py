import aoc

import numpy as np
import pandas as pd


day = 8

pinput = aoc.input(day)
inputs = pinput.split('\n')[:-1]

# Assumes all patterns are available in the input

def one(patterns):
    for p in patterns:
        if len(p) == 2:
            return p

def seven(patterns):
    for p in patterns:
        if len(p) == 3:
            return p

def four(patterns):
    for p in patterns:
        if len(p) == 4:
            return p

def eight(patterns):
    for p in patterns:
        if len(p) == 8:
            return p

def six_or_nine_or_zero(patterns):
    return [p for p in patterns if len(p) == 6]

def two_or_three_or_five(patterns):
    return [p for p in patterns if len(p) == 5]

def a(patterns):
    return [l for l in seven(patterns) if l not in one(patterns)][0]

def bd(patterns):
    return [l for l in four(patterns) if l not in one(patterns)]

def cf(patterns):
    return one(patterns)

def cde(patterns):
    res = ""
    p = six_or_nine_or_zero(patterns)
    for l in p[0]:
        if (l not in p[1]) or (l not in p[2]):
            res += l
    for l in p[1]:
        if (l not in p[0]) or (l not in p[2]):
            res += l
    for l in p[2]:
        if (l not in p[1]) or (l not in p[0]):
            res += l
    return "".join(set(res))

def determine_cf(patterns):
    for l in cf(patterns):
        if l in cde(patterns):
            return {"c": l, "f": [m for m in cf(patterns) if m != l][0]}
        else:
            return {"f": l, "c": [m for m in cf(patterns) if m != l][0]}

def determine_bd(patterns):
    for l in bd(patterns):
        if l in cde(patterns):
            return {"d": l, "b": [m for m in bd(patterns) if m != l][0]}
        else:
            return {"b": l, "d": [m for m in bd(patterns) if m != l][0]}

def cipher(patterns):
    letters = {}
    letters['a'] = a(patterns)
    letters.update(determine_cf(patterns))
    letters.update(determine_bd(patterns))
    c = letters['c']
    d = letters['d']
    for l in cde(patterns):
        if l != c and l != d:
            letters['e'] = l
    for v in 'abcdefg':
        if v not in letters.values():
            letters['g'] = v
    return letters

tablevals = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

def decode(patterns, outputs):
    val = 0
    coef = 1000
    letters = cipher(patterns)
    decipher = {v: k for k, v in letters.items()}
    for output in outputs:
        deciphered = ''.join(sorted([decipher[l] for l in output]))
        val += coef * tablevals[deciphered]
        coef /= 10
    return int(val)

total = 0
for input in inputs:
    sigpatterns = input.split('|')[0].strip().split(' ')
    outputvals = input.split('|')[1].strip().split(' ')

    total += decode(sigpatterns, outputvals)

print(total)

# aoc.submit(day, 2, total)