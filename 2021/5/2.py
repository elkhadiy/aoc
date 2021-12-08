#/usr/bin/env python3

import numpy as np
import requests as rq
import requests_cache
requests_cache.install_cache("/home/yelkhadi/.aoc/cache")

day = 5
session_cookie_location = "/home/yelkhadi/.aoc/secret"

with open(session_cookie_location, "r") as session:
    headers = {"Cookie": session.readline()[:-1]}
input = rq.get(f"https://adventofcode.com/2021/day/{day}/input", headers=headers).text

lines = np.array([
    int(coord)
    for line in input.splitlines()
    for point in line.split(' -> ')
    for coord in point.split(',')
]).reshape(-1, 2, 2)

map = np.zeros((lines[:,:,0].max() + 1, lines[:,:,1].max() + 1))

for line in lines:
    (x1, y1), (x2, y2) = line
    N = max(abs(x1 - x2) + 1, abs(y1 - y2) + 1)
    linemask = np.zeros((lines[:,:,0].max() + 1, lines[:,:,1].max() + 1))
    linemask[
        np.linspace(y1, y2, N).astype(int),
        np.linspace(x1, x2, N).astype(int)
    ] = 1
    map += linemask

print(map.astype(int))

print(np.where(map >= 2)[0].size)