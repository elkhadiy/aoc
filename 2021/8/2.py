import aoc

import numpy as np
import pandas as pd


day = 8

inputs = aoc.input(day).split('\n')[:-1]

# Assumes all patterns are available in the input

one   = lambda codes: set(codes[[len(code) for code in codes].index(2)])
seven = lambda codes: set(codes[[len(code) for code in codes].index(3)])
four  = lambda codes: set(codes[[len(code) for code in codes].index(4)])
eight = lambda codes: set(codes[[len(code) for code in codes].index(8)])

six_nine_zero = lambda codes: [set(code) for code in codes if len(code) == 6]

cf  = lambda codes: one(codes)
bd  = lambda codes: four(codes) - one(codes)
cde = lambda codes: set('abcdefg') - set.intersection(*six_nine_zero(codes))

a = lambda codes: seven(codes) - one(codes)
c = lambda codes: cde(codes) & cf(codes)
f = lambda codes: cf(codes) - c(codes)
d = lambda codes: bd(codes) & cde(codes)
b = lambda codes: bd(codes) - d(codes)
e = lambda codes: cde(codes) - c(codes) - d(codes)
g = lambda codes: set('abcdefg') - a(codes) - b(codes) - c(codes) - d(codes) - e(codes) - f(codes)

enc = lambda codes: {
    'a': next(iter(a(codes))),
    'b': next(iter(b(codes))),
    'c': next(iter(c(codes))),
    'd': next(iter(d(codes))),
    'e': next(iter(e(codes))),
    'f': next(iter(f(codes))),
    'g': next(iter(g(codes)))
}

dec = lambda codes: {v: k for k, v in enc(codes).items()}

segments = {
    'abcefg' : '0',
    'cf'     : '1',
    'acdeg'  : '2',
    'acdfg'  : '3',
    'bcdf'   : '4',
    'abdfg'  : '5',
    'abdefg' : '6',
    'acf'    : '7',
    'abcdefg': '8',
    'abcdfg' : '9'
}

def decode(codes, outputs):
    deciphered = ''
    decipher = dec(codes)
    for output in outputs:
        deciphered += segments[''.join(sorted([decipher[l] for l in output]))]
    return int(deciphered)

total = 0
for input in inputs:
    sigpatterns = input.split('|')[0].strip().split(' ')
    outputvals = input.split('|')[1].strip().split(' ')

    total += decode(sigpatterns, outputvals)

print(total)

# aoc.submit(day, 2, total)