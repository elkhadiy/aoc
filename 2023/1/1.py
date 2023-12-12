import aoc


input = aoc.input(1)

digits = [
    "".join(c for c in line if c.isdigit())
    for line in input.split("\n")
    if line is not None
]

calibration_values = [
    int("".join([d[0], d[-1]]))
    for d in digits
    if d != ''
]

aoc.submit(1, 1, sum(calibration_values))
