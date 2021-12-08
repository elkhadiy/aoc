import aoc

import numpy as np
import pandas as pd


day = 8

inputs = aoc.input(day).split('\n')[:-1]

count = 0

for input in inputs:
    sigpatterns = input.split('|')[0].strip().split(' ')
    outputvals = input.split('|')[1].strip().split(' ')
    count += len([ len(o) for o in outputvals if len(o) in [2, 4, 3, 7] ])

print(count)

#aoc.submit(day, 1, count)