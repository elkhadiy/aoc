#/usr/bin/env python3

import numpy as np
import requests as rq
import requests_cache
requests_cache.install_cache("/home/yelkhadi/.aoc/cache")

day = 4
session_cookie_location = "/home/yelkhadi/.aoc/secret"

with open(session_cookie_location, "r") as session:
    headers = {"Cookie": session.readline()[:-1]}
input = rq.get(f"https://adventofcode.com/2021/day/{day}/input", headers=headers).text

input = input.split('\n\n')

numbers = np.array([int(number) for number in input[0].split(',')])

boards = np.array([
    int(number)
    for board in input[1:]
    for number in board.replace('\n', ' ').replace('  ', ' ').strip().split(' ')
]).reshape(-1, 5, 5)

tracker = np.zeros_like(boards)

check = lambda tracker: np.where(np.array([[board.sum(axis=0), board.sum(axis=1)] for board in tracker]) == 5)

def feed_number(tracker, boards, number):
    tracker[np.where(boards == number)] = 1

for number in numbers:
    feed_number(tracker, boards, number)
    lookup = np.array(check(tracker)).transpose()
    if lookup.size:
        print(lookup[0][0])
        break

winning_board = lookup[0][0]

sum_all_unmarked_numbers = boards[winning_board].sum() - (tracker[winning_board] * boards[winning_board]).sum()

score = sum_all_unmarked_numbers * number

print(score)