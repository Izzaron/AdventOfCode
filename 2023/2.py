from typing import List
from enum import Enum

class Game:
    def __init__(self, id: int) -> None:
        self.id: int = int(id)
        self.max_cubes = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        self.min_cubes = dict()
        
f = open('2.txt')

games: List[Game] = list()

for line in f.readlines():
    game_str,cubes_str = line.split(':')

    game = Game(game_str.split()[1])
    games.append(game)

    sets = cubes_str.split(';')
    for cube_set in sets:
        for nrAndCube in cube_set.split(','):
            nr,color = nrAndCube.split()
            game.max_cubes[color] = max(game.max_cubes[color],int(nr))

id_sum = 0
for game in games:
    if game.max_cubes['red'] <= 12 and game.max_cubes['green'] <= 13 and game.max_cubes['blue'] <= 14:
        id_sum += game.id

print(id_sum)

id_prod = 0
for game in games:
    game_prod = game.max_cubes['red'] * game.max_cubes['green'] * game.max_cubes['blue']
    id_prod += game_prod

print(id_prod)