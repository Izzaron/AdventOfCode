input_file = __file__.replace('.py','.txt')
test_file = __file__.replace('.py','test.txt')
test_file2 = __file__.replace('.py','test2.txt')

class Valley:
    def __init__(self, width: int, height: int, winds: list[tuple[int,int,int]],entrances: set[tuple[int,int]]) -> None:
        self.width = width
        self.height = height
        self.winds = winds
        self.entrances = entrances
    
    def winds_at(self,minute: int) -> set[tuple[int,int]]:
        return_winds = set()
        for wind in winds:
            if wind[2] == 0:
                return_winds.add(( (wind[0]+minute)%self.width  ,   wind[1]                         ))
            elif wind[2] == 1:
                return_winds.add((  wind[0]                     ,  (wind[1]-minute)%self.height     ))
            elif wind[2] == 2:
                return_winds.add(( (wind[0]-minute)%self.width  ,   wind[1]                         ))
            elif wind[2] == 3:
                return_winds.add((  wind[0]                     ,  (wind[1]+minute)%self.height     ))
            else:
                raise ValueError(wind[2])
        return return_winds
    
    def in_bounds(self,x: int,y: int) -> bool:
        if (x,y) in self.entrances:
            return True
        if x >= 0 and y >= 0 and x < self.width and y < self.height:
            return True
        return False
    
    def find_shortest_path(self,start: tuple[int,int],goal: tuple[int,int],start_min: int) -> int:
        minute = start_min + 1
        possible_positions = {start}
        directions = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]
        while True:
            winds = self.winds_at(minute)
            candidate_positions = set()
            for position in possible_positions:
                for direction in directions:
                    x,y = position[0]+direction[0] , position[1]+direction[1]
                    if (x,y) == goal:
                        return minute
                    if self.in_bounds(x,y) and (x,y) not in winds:
                        candidate_positions.add((x,y))
            possible_positions = candidate_positions
            minute += 1

if __name__ == "__main__":

    with open(input_file) as puzzle_input:
        input_lines = [list(line.strip()) for line in puzzle_input.readlines()]
    height = len(input_lines) - 2
    width = len(input_lines[0]) - 2
    winds = []
    for y,line in enumerate(input_lines[1:-1]):
        for x,char in enumerate(line[1:-1]):
            if char == '>':
                winds.append((x,y,0))
            elif char == '^':
                winds.append((x,y,1))
            elif char == '<':
                winds.append((x,y,2))
            elif char == 'v':
                winds.append((x,y,3))
            elif char in '.#':
                pass
            else:
                raise ValueError(char)

    start = (0,-1)
    goal = (width - 1,height)
    
    valley = Valley(width,height,winds,{start,goal})
    
    trip1_time = valley.find_shortest_path(start,goal,0)
    trip2_time = valley.find_shortest_path(goal,start,trip1_time)
    trip3_time = valley.find_shortest_path(start,goal,trip2_time)
    print(trip1_time,trip2_time-trip1_time,trip3_time-trip2_time,trip3_time)