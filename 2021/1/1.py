import aoc

import numpy as np

day = 1

measurements_req = aoc.input(day)

measurements = np.array(measurements_req.text.split('\n')[:-1]).astype(int)

increased = (measurements[:-1] - measurements[1:]) < 0

print(sum(increased))