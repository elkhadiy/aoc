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

print(int(np.sum(np.abs(crabs - np.median(crabs)))))
