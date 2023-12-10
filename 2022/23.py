from coordinates import Coordinate,Direction

input_file = __file__.replace('.py','.txt')
test_file = __file__.replace('.py','test.txt')
small_test_file = __file__.replace('.py','small.txt')

class Elf:
    def __init__(self,start_position: Coordinate) -> None:
        self.position: Coordinate = start_position
        self.proposed_move = None
    
    def __repr__(self) -> str:
        return 'E'+self.position.__repr__()
    
    def __str__(self) -> str:
        return 'E'+self.position.__str__()

    def has_neighbours(self,elves: dict[tuple[int,int],'Elf']) -> bool:
        surrounding = [(self.position.x + dx,self.position.y + dy) for dx in [-1,0,1] for dy in [-1,0,1] if not (dx == 0 and dy == 0)]
        if any(pos in elves for pos in surrounding):
            return True
        return False

    def is_direction_valid(self,direction: Direction, elves: dict[tuple[int,int],'Elf']) -> bool:
        test_coord1 = self.position.getCoordinateInDirection(direction,flip_y=True)
        test_coord2 = test_coord1.getCoordinateInDirection(direction + 90,flip_y=True)
        test_coord3 = test_coord1.getCoordinateInDirection(direction - 90,flip_y=True)
        checkpoints = [test_coord1.asTuple(),test_coord2.asTuple(),test_coord3.asTuple()]
        if any(checkpoint in elves for checkpoint in checkpoints):
                return False
        return True
    
    def wants_to_move(self,direction_order: list[Direction], elves: dict[tuple[int,int],'Elf']) -> bool:
        if not self.has_neighbours(elves):
            self.proposed_move = self.position
            return False
        for direction in direction_order:
            if self.is_direction_valid(direction,elves):
                self.proposed_move = self.position.getCoordinateInDirection(direction,flip_y=True)
                return True
        self.proposed_move = self.position
        return True

def print_elves(elves: dict[tuple[int,int],Elf]) -> None:
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    for x,y in elves.keys():
        min_x = min(min_x,x)
        max_x = max(max_x,x)
        min_y = min(min_y,y)
        max_y = max(max_y,y)
    
    karta = [['.' for _ in range (min_x,max_x+1)] for _ in range(min_y,max_y+1)]
    for x,y in elves.keys():
        karta[y][x] = '#'

    for row in karta:
        print(''.join(row))
    
    print('Empty spaces:', (max_x-min_x+1) * (max_y-min_y+1) - len(elves))

if __name__ == "__main__":

    with open(input_file) as puzzle_input:
        blueprint = [list(i.strip()) for i in puzzle_input.readlines()]

    elves: dict[tuple[int,int],Elf] = dict()

    for y,row in enumerate(blueprint):
        for x,elf in enumerate(row):
            if elf == '#':
                elves[(x,y)] = Elf(Coordinate(x,y))

    all_elves = list(elves.values())

    print_elves(elves)

    directions = [Direction(90),Direction(270),Direction(180),Direction(0)]
    dir_count = len(directions)
    first_direction = 0

    any_wanted_to_move = True

    round_nr = 0
    while(any_wanted_to_move):
        any_wanted_to_move = False
        direction_order = [directions[(i+first_direction)%dir_count] for i in range(dir_count)]
        proposed_moves: dict[tuple[int,int],list[Elf]] = dict()
        for elf in elves.values():
            if elf.wants_to_move(direction_order,elves):
                any_wanted_to_move = True
            if not elf.proposed_move.asTuple() in proposed_moves:
                proposed_moves[elf.proposed_move.asTuple()] = []
            proposed_moves[elf.proposed_move.asTuple()].append(elf)
        
        for move_elves in proposed_moves.values():
            if len(move_elves) > 1:
                for elf in move_elves:
                    elf.proposed_move = None
            else:
                move_elves[0].position = move_elves[0].proposed_move
                move_elves[0].proposed_move = None
        
        elves = {elf.position.asTuple():elf for elf in all_elves}
        first_direction += 1
        round_nr += 1
        # if round_nr == 10:
        #     break

    print_elves(elves)
    print('Number of rounds:',round_nr)