import aoc

import numpy as np
import pandas as pd

day = 1

measurements_req = aoc.input(day)

measurements = np.array(measurements_req.text.split('\n')[:-1]).astype(int)

measurements = pd.Series(measurements).rolling(3).sum()[2:]

increased = (measurements[:-1].values - measurements[1:].values) < 0

print(sum(increased))