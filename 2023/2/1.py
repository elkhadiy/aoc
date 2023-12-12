import numpy as np

import aoc

input = aoc.input(2).strip().splitlines()

# input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".strip().splitlines()


def game_matrix(game):
    """
     R, G, B
    [x  x  x]
    [x  x  x]
    [  ...  ]
    """
    game = game.split(":")[1]
    rounds = game.split(";")
    M = None
    obsdict = {'red': 0, 'green': 1, 'blue': 2}
    for round in rounds:
        obs = np.zeros(3)
        for tirage in round.split(','):
            color = tirage.split()[1].strip()
            number = int(tirage.split()[0].strip())
            obs[obsdict[color]] = number
        if M is not None:
            M = np.concatenate((M, [obs]), axis=0)
        else:
            M = np.array([obs])
    return M


def possible(game, maximums):
    return np.all(game.max(axis=0) <= maximums)


maximums = (12, 13, 14)


possible_games = [
    possible(game_matrix(game), maximums)
    for game in input
]

answer = np.sum(np.where(possible_games)[0] + 1)

print(answer)

aoc.submit(2, 1, answer)
