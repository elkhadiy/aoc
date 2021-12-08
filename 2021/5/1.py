import aoc

import numpy as np

day = 5

input = aoc.input(day)

lines = np.array([
    int(coord)
    for line in input.splitlines()
    for point in line.split(' -> ')
    for coord in point.split(',')
]).reshape(-1, 2, 2)

map = np.zeros((lines[:,:,0].max() + 1, lines[:,:,1].max() + 1))

for line in lines:
    (x1, y1), (x2, y2) = line
    if x1 == x2 or y1 == y2:
        N = max(abs(x1 - x2) + 1, abs(y1 - y2) + 1)
        linemask = np.zeros((lines[:,:,0].max() + 1, lines[:,:,1].max() + 1))
        linemask[
            np.linspace(y1, y2, N).astype(int),
            np.linspace(x1, x2, N).astype(int)
        ] = 1
        map += linemask

print(map.astype(int))

print(np.where(map >= 2)[0].size)