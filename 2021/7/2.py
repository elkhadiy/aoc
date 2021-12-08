import aoc

import numpy as np

day = 7

input = aoc.input(day)

crabs = np.array([int(crab) for crab in input.split(',')])

conso = np.zeros((crabs.shape[0], crabs.max() + 1), dtype=int)

def conso_func(n):
    return n * (n+1) / 2

for i in range(crabs.shape[0]):
    for j in range(crabs.max() + 1):
        conso[i, j] = conso_func(abs(crabs[i] - (crabs.max() - j)))

# np.set_printoptions(linewidth=150)
# print(pd.DataFrame(conso, columns=reversed(range(crabs.max()+1)), index=crabs))
# print("config:", crabs.max() - np.argmin(conso.sum(axis=0)))
print("fuel  :", np.min(conso.sum(axis=0)))
