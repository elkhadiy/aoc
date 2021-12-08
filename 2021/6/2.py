import aoc

import numpy as np

from functools import lru_cache

day = 6

input = aoc.input(day)

fishs = [int(i) for i in input.split(',')]

@lru_cache
def fish(n, d):
    return 1 + sum([ fish(8, d - (n+1) - 7*i) for i in range(int((d + 6 - n)/7)) ])

data = np.array([fish(n, 256) for n in np.unique(fishs)])

print(sum(data * np.unique(fishs, return_counts=True)[1]))
