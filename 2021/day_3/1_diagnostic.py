#/usr/bin/env python3

import numpy as np
import requests as rq
import requests_cache
requests_cache.install_cache("/home/yelkhadi/.aoc/cache")

day = 3
session_cookie_location = "/home/yelkhadi/.aoc/secret"

with open(session_cookie_location, "r") as session:
    headers = {"Cookie": session.readline()[:-1]}
diag_txt = rq.get(f"https://adventofcode.com/2021/day/{day}/input", headers=headers).text


bit_width = len(diag_txt.split('\n')[0])

diagnostic = np.frombuffer(bytes(diag_txt, 'utf-8').replace(b'\n', b''), dtype='u1')
diagnostic = diagnostic - ord('0')
diagnostic = diagnostic.reshape(-1, bit_width)

majorite = lambda arr: int(sum(arr) >= arr.shape[0] / 2)

oxygen = diagnostic.copy()
col = 0

while oxygen.shape[0] > 1:
    oxygen = oxygen[np.where(oxygen[:,col] == majorite(oxygen[:,col]))]
    col += 1

oxygen = oxygen[0]


co2 = diagnostic.copy()
col = 0

while co2.shape[0] > 1:
    co2 = co2[np.where(co2[:,col] != majorite(co2[:,col]))]
    col += 1

co2 = co2[0]


to_decimal = lambda arr: sum(2**i * b for i, b in enumerate(reversed(arr)))

print(to_decimal(oxygen) * to_decimal(co2))

