#/usr/bin/env python3

import requests as rq
import requests_cache
requests_cache.install_cache("/home/yelkhadi/.aoc/cache")

day = 2
session_cookie_location = "/home/yelkhadi/.aoc/secret"

with open(session_cookie_location, "r") as session:
    headers = {"Cookie": session.readline()[:-1]}
moves_req = rq.get(f"https://adventofcode.com/2021/day/{day}/input", headers=headers).text

moves = [
    (move.split(' ')[0], int(move.split(' ')[1]))
    for move in moves_req.split('\n')[:-1]
    ]

forward = 0
depth = 0

for move in moves:
    if move[0] == "forward": forward += move[1]
    if move[0] == "up":      depth -= move[1]
    if move[0] == "down":    depth += move[1]

print((forward, depth), forward * depth)