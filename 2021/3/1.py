import aoc

import numpy as np

day = 3

diag_txt = aoc.input(day)

bit_width = len(diag_txt.split('\n')[0])

diagnostic = np.frombuffer(bytes(diag_txt, 'utf-8').replace(b'\n', b''), dtype='u1')
diagnostic = diagnostic - ord('0')
diagnostic = diagnostic.reshape(-1, bit_width)

majorite = lambda arr: int(sum(arr) >= arr.shape[0] / 2)

gamma = np.array([ majorite(diagnostic[:,i]) for i in range(bit_width) ])

epsilon = np.logical_not(gamma).astype(int)

to_decimal = lambda arr: sum(2**i * b for i, b in enumerate(reversed(arr)))

print(to_decimal(gamma) * to_decimal(epsilon))

