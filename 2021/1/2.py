#/usr/bin/env python3

import numpy as np
import pandas as pd
import requests as rq
import requests_cache
requests_cache.install_cache("/home/yelkhadi/.aoc/cache")

day = 1
session_cookie_location = "/home/yelkhadi/.aoc/secret"

with open(session_cookie_location, "r") as session:
    headers = {"Cookie": session.readline()[:-1]}
measurements_req = rq.get(f"https://adventofcode.com/2021/day/{day}/input", headers=headers)

measurements = np.array(measurements_req.text.split('\n')[:-1]).astype(int)

measurements = pd.Series(measurements).rolling(3).sum()[2:]

increased = (measurements[:-1].values - measurements[1:].values) < 0

print(sum(increased))