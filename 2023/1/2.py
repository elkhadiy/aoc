from functools import lru_cache

import aoc


input = aoc.input(1).strip().splitlines()

# input = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen""".strip().splitlines()

rules = {
    "one":   "1",
    "two":   "2",
    "three": "3",
    "four":  "4",
    "five":  "5",
    "six":   "6",
    "seven": "7",
    "eight": "8",
    "nine":  "9"
}


@lru_cache
def first_digit(s, i=0):
    if s[i:i+1].isdigit():
        return s[i:i+1]
    for k, v in rules.items():
        if k in s[:i+1]:
            return v
    if i+1 == len(s):
        return None
    return first_digit(s, i+1)


@lru_cache
def last_digit(s, i):
    if s[i-1:i].isdigit():
        return s[i-1:i]
    for k, v in rules.items():
        if k in s[i-1:]:
            return v
    if i-1 == 0:
        return None
    return last_digit(s, i-1)


calibration_values = [
    int("".join([first_digit(d), last_digit(d, len(d))]))
    for d in input
]


print(sum(calibration_values))
aoc.submit(1, 2, sum(calibration_values))
