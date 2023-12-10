import os
import copy
from coordinates import Coordinate, Direction

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Karta:
    
    def __init__(self,visited: set[Coordinate]) -> None:
        self.min_x = None
        self.max_x = None
        self.min_y = None
        self.max_y = None
        for coordinate in visited:
            self.min_x = coordinate[0] if self.min_x == None else min(self.min_x,coordinate[0])
            self.max_x = coordinate[0] if self.max_x == None else max(self.max_x,coordinate[0])
            self.min_y = coordinate[1] if self.min_y == None else min(self.min_y,coordinate[1])
            self.max_y = coordinate[1] if self.max_y == None else max(self.max_y,coordinate[1])
        self.karta = [['.' for _ in range(self.min_x,self.max_x+1)] for _ in range(self.min_y,self.max_y+1)]
        # print(self.karta)
        for coordinate in visited:
            # print(coordinate[0],coordinate[1])
            self.karta[coordinate[1]-self.min_y][coordinate[0]-self.min_x] = '#'

    def print(self):
        for row in reversed(self.karta):
            print(''.join(row))

directions = {
    'R': Direction(0),
    'U': Direction(90),
    'L': Direction(180),
    'D': Direction(270),
}

def update_tail(head: Coordinate, tail: Coordinate):
    diff_x = head.x - tail.x
    diff_y = head.y - tail.y
    move_x = 0 if diff_x == 0 else int(diff_x/abs(diff_x))
    move_y = 0 if diff_y == 0 else int(diff_y/abs(diff_y))
    if abs(diff_x) > 1 or abs(diff_y) > 1:
        tail += Coordinate(move_x,move_y)

if __name__ == "__main__":

    with open(os.path.join(__location__, 'input9.txt')) as puzzle_input:

        lines = puzzle_input.readlines()

    nr_of_knots = 10

    knots = [Coordinate(0,0) for _ in range(nr_of_knots)]

    visited: set[Coordinate] = set()

    visited.add(knots[-1].asTuple())

    for line in lines:
        command = line.strip().split()

        for _ in range(int(command[1])):

            knots[0].stepInDirection( directions[command[0]] )

            for i in range(len(knots)-1):
                update_tail(knots[i],knots[i+1])

            visited.add(knots[-1].asTuple())
    
    Karta(visited).print()
    print(len(visited))