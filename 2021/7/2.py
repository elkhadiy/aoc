#/usr/bin/env python3

import numpy as np
import requests as rq
import requests_cache
requests_cache.install_cache("/home/yelkhadi/.aoc/cache")

day = 7
session_cookie_location = "/home/yelkhadi/.aoc/secret"

with open(session_cookie_location, "r") as session:
    headers = {"Cookie": session.readline()[:-1]}
input = rq.get(f"https://adventofcode.com/2021/day/{day}/input", headers=headers).text

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
