import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Karta:
    def __init__(self) -> None:
        self.karta: list[set[int]] = [[]]
        self.sand: list[set[int]] = [[]]

    def add_section(self,section_str: str):
        section = [(int(c.split(',')[0]),int(c.split(',')[1])) for c in [s.strip() for s in section_str.split('->')]]
        for i in range(len(section)-1):
            self.add_line(section[i],section[i+1])
    
    def add_line(self, from_point: tuple[int,int], to_point: tuple[int,int]):
        while(len(self.karta) < max(from_point[1],to_point[1])+1):
            self.karta.append(set())
        for x in range(min(from_point[0],to_point[0]),max(from_point[0],to_point[0])+1):
            for y in range(min(from_point[1],to_point[1]),max(from_point[1],to_point[1])+1):
                self.karta[y].add(x)

    def init_sand(self):
        self.sand = [set() for _ in range(len(self.karta)+2)]

    def sand_count(self):
        return sum(len(row) for row in self.sand)

    def simulate(self):
        self.init_sand()
        rtn = True
        while(rtn):
            rtn = self.simulate_grain()
    
    def at(self,x,y):
        if x < 0 or y < 0 or y>len(self.sand):
            return '.'
        if x in self.sand[y]:
            return 'o'
        if y == len(self.karta):
            return '.'
        if y > len(self.karta):
            return '#'
        if x in self.karta[y]:
            return '#'
        else:
            return '.'
    
    def simulate_grain(self):
        sand_pos = (500,0)
        if self.at(*sand_pos) != '.':
            return False
        while(True):
            if self.at(sand_pos[0],sand_pos[1]+1) == '.':
                sand_pos = (sand_pos[0],sand_pos[1]+1)
            elif self.at(sand_pos[0]-1,sand_pos[1]+1) == '.':
                sand_pos = (sand_pos[0]-1,sand_pos[1]+1)
            elif self.at(sand_pos[0]+1,sand_pos[1]+1) == '.':
                sand_pos = (sand_pos[0]+1,sand_pos[1]+1)
            else:
                self.sand[sand_pos[1]].add(sand_pos[0])
                return True

    def print(self):
        min_x = min(i for row in self.karta+self.sand for i in row)
        max_x = max(i for row in self.karta+self.sand for i in row)
        for y in range(len(self.karta)):
            print(y,end=' ')
            for x in range(min_x,max_x+1):
                if y == 0 and x == 500:
                    print('+',end='')
                    continue
                if x in self.karta[y]:
                    print('#',end='')
                elif x in self.sand[y]:
                    print('o',end='')
                else:
                    print('.',end='')
            print()
        print(len(self.karta),end=' ')
        for x in range(min_x,max_x+1):
            print('0',end='') if x in self.sand[len(self.karta)] else print('.',end='')
        print()
        print(len(self.karta)+1,end=' ')
        for x in range(min_x,max_x+1):
            print('#',end='')
        print()

if __name__ == "__main__":

    karta = Karta()

    with open(os.path.join(__location__, 'input14.txt')) as puzzle_input:

        for line in puzzle_input:
            karta.add_section(line.strip())
    
    karta.simulate()
    karta.print()
    print(karta.sand_count())