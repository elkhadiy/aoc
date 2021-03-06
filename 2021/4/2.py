import aoc

import numpy as np


day = 4

input = aoc.input(day).split('\n\n')

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


boards_bingod = []

state = {}

for number in numbers:
    feed_number(tracker, boards, number)
    lookups = np.array(check(tracker)).transpose()
    for lookup in lookups:

        idx = lookup[0]

        if idx not in boards_bingod:

            boards_bingod.append(idx)

            winning_board = boards[idx].copy()
            winning_tracker = tracker[idx].copy()
            winning_number = number

            sum_all_unmarked_numbers = winning_board.sum() - (winning_tracker * winning_board).sum()
            board_score = sum_all_unmarked_numbers * winning_number

            state[idx] = {
                "number": idx,
                "board": winning_board,
                "tracker": winning_tracker,
                "score": board_score
            }

print(boards_bingod)

print(state[boards_bingod[0]])
print(state[boards_bingod[-1]])
