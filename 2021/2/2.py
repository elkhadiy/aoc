import aoc

day = 2

moves_req = aoc.input(day)

moves = [
    (move.split(' ')[0], int(move.split(' ')[1]))
    for move in moves_req.split('\n')[:-1]
    ]

pos = [0, 0, 0]
forward = 0
depth = 0
aim = 0

for move in moves:
    if move[0] == "forward":
        forward += move[1]
        depth += aim * move[1]

    if move[0] == "up":   aim -= move[1]
    if move[0] == "down": aim += move[1]

print((forward, depth), aim, forward * depth)