import aoc

import numpy as np

day = 7

input = aoc.input(day)

crabs = np.array([int(crab) for crab in input.split(',')])

print(int(np.sum(np.abs(crabs - np.median(crabs)))))
