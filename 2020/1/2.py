import aoc

from itertools import combinations
from math import prod

day = 1
level = 2
year = 2020
input = aoc.input(day, year)

entries = [int(entry) for entry in input.split('\n')[:-1]]
sum_entries = {
    sum(combination): combination
    for combination in combinations(entries, 3)
}

aoc.submit(day, level, prod(sum_entries[2020]), year)