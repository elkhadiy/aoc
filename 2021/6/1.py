#/usr/bin/env python3

import numpy as np
import requests as rq
import requests_cache
requests_cache.install_cache("/home/yelkhadi/.aoc/cache")

day = 6
session_cookie_location = "/home/yelkhadi/.aoc/secret"

with open(session_cookie_location, "r") as session:
    headers = {"Cookie": session.readline()[:-1]}
input = rq.get(f"https://adventofcode.com/2021/day/{day}/input", headers=headers).text


fishs = [int(i) for i in input.split(',')]

def fish(n, d):
    return 1 + sum([ fish(8, d - (n+1) - 7*i) for i in range(int((d + 6 - n)/7)) ])

data = np.array([fish(n, 256) for n in np.unique(fishs)])

print(sum(data * np.unique(fishs, return_counts=True)[1]))
