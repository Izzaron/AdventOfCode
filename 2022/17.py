from itertools import cycle
import time
import datetime
from math import lcm

input_file = __file__.replace('.py','.txt')
test_file = __file__.replace('.py','test.txt')

class Rock:
    def __init__(self,pattern,repr) -> None:
        self.pattern    :list[list[int]] = list(reversed(pattern))
        self.repr = repr
        self.height = len(pattern)
        self.width = len(pattern[0])
        self.x = 0
        self.y = 0
        self.bottom_bounds = [(i,0) if s else (i,1) for i,s in enumerate(self.pattern[0])]
        self.left_bounds = [0] * len(self.pattern)
        for j,row in enumerate(self.pattern):
            for i,pixel in enumerate(row):
                if pixel:
                    self.left_bounds[j] = (i,j)
                    break
        self.right_bounds = [0] * len(self.pattern)
        for j,row in reversed(list(enumerate(self.pattern))):
            for i,pixel in reversed(list(enumerate(row))):
                if pixel:
                    self.right_bounds[j] = (i,j)
                    break
    
    def print(self):
        for row in self.pattern:
            print(''.join([str(i) for i in row]))

    def __str__(self) -> str:
        return self.__repr__()
    
    def __repr__(self) -> str:
        return self.repr

    def lower_bounds(self):
        return [(i+self.x,j+self.y) for i,j in self.bottom_bounds]
    
    def leftward_bounds(self):
        return [(i+self.x,j+self.y) for i,j in self.left_bounds]
    
    def rightward_bounds(self):
        return [(i+self.x,j+self.y) for i,j in self.right_bounds]
    
    def push(self,jet: str):
        if jet == '>':
            self.x += 1
        elif jet == '<':
            self.x -= 1
        else:
            raise ValueError('wind: \"{}\"'.format(jet))
    
    def fall(self):
        self.y -= 1

class Chamber:
    def __init__(self,jet_pattern,rock_pattern) -> None:
        
        self.jet_iterator = cycle(jet_pattern)
        self.rock_iterator = cycle(rock_pattern)
        self.chamber = []
        self.highestRock = -1
    
    def height(self) -> int:
        return self.highestRock + 1
    
    def is_empty_at(self,x,y) -> bool:
        if y<0 or x<0 or x>6:
            return False
        if y>=len(self.chamber):
            return True
        return self.chamber[y][x] == 0
    
    def next_rock(self) -> Rock:
        return next(self.rock_iterator)
    
    def next_jet(self) -> str:
        return next(self.jet_iterator)
    
    def is_at_vertical_rest(self,rock: Rock) -> bool:
        return any(not self.is_empty_at(x,y-1) for x,y in rock.lower_bounds())
    
    def is_at_horizontal_rest(self, rock: Rock, jet: str) -> bool:
        if jet == '>':
            return any(not self.is_empty_at(x+1,y) for x,y in rock.rightward_bounds())
        elif jet == '<':
            return any(not self.is_empty_at(x-1,y) for x,y in rock.leftward_bounds())
        else:
            raise ValueError('wind: \"{}\"'.format(jet))

    def imprint(self,rock: Rock) -> None:
        for _ in range(len(self.chamber),rock.y+rock.height):
            self.chamber.append([0]*7)
        for j,row in enumerate(rock.pattern):
            for i,symbol in enumerate(row):
                self.chamber[j+rock.y][i+rock.x] = self.chamber[j+rock.y][i+rock.x] | symbol

    def fall_rock(self) -> None:
        rock = self.next_rock()
        rock.x = 2
        rock.y = self.highestRock + 4
        rock.push(self.next_jet())
        while(not self.is_at_vertical_rest(rock)):
            rock.fall()
            jet = self.next_jet()
            if not self.is_at_horizontal_rest(rock,jet):
                rock.push(jet)
        self.highestRock = max(self.highestRock,rock.y+rock.height-1)
        self.imprint(rock)

    def print(self,rows: int = None):
        if rows == None:
            rows = self.height()
        for i,row in reversed(list(enumerate(self.chamber[-rows:]))):
            print(''.join(['#' if i else '.' for i in row]),i+1+self.height()-rows)

    def topography(self) -> tuple[int,int,int,int,int,int,int]:
        rtn = [0] * 7
        for col in range(7):
            for i,row in enumerate(reversed(self.chamber)):
                if row[col]:
                    i -= 1
                    break
            rtn[col] = i+1
                    
        return tuple(rtn)

if __name__ == "__main__":

    rock_patterns = [
        [[1,1,1,1]],
        [[0,1,0],[1,1,1],[0,1,0]],
        [[0,0,1],[0,0,1],[1,1,1]],
        [[1],[1],[1],[1]],
        [[1,1],[1,1]],
    ]

    rock_reprs = [
        '-',
        '+',
        '┘',
        '|',
        '■',
    ]

    with open(input_file) as puzzle_input:
        jet_pattern = puzzle_input.readline()
        rock_pattern = [Rock(rock_patterns[i],rock_reprs[i]) for i in range(len(rock_patterns))]
        chamber = Chamber(jet_pattern,rock_pattern)

    # part 1 + estimate with conventional method
    # rock_count = 2022
    # start_time = time.time()
    # for _ in range(rock_count):
    #     chamber.fall_rock()
    # end_time = time.time()
    # total_time = end_time - start_time
    # print(total_time,chamber.height())
    # print('estimate',str(datetime.timedelta(seconds=(total_time/rock_count*1e12))))

    # part 2 analysis
    rep = lcm( len(jet_pattern) , len(rock_pattern) )
    # rock_count = rep*680
    # repeats = dict()
    # for i in range(rock_count):
    #     chamber.fall_rock()
    #     if i%rep == 0:
    #         print('rep',i//rep,)
    #         topo = chamber.topography()
    #         if topo not in repeats:
    #             repeats[topo] = []
    #         repeats[topo].append((i//rep,chamber.height()))
    
    # for repeat in repeats.items():
    #     print(repeat)

    # part 2 computation
    period = rep*338
    period_height_diff = 26710877

    raw_rock_count = 1e12
    skip_count = raw_rock_count//period
    comp_rock_count = raw_rock_count%period
    print('computing',comp_rock_count//rep,'reps')
    for i in range(int(comp_rock_count)):
        if i%rep == 0:
            print('rep',i//rep)
        chamber.fall_rock()
    print(chamber.height() + skip_count*period_height_diff)