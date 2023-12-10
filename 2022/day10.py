import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class CommunicationSystem:
    
    def __init__(self) -> None:
        self.cycle = 0
        self.X = 1
        self.next_check = 20
        self.px_min = 0
        self.px_max = 39
        self.row_min = 0
        self.row_max = 5
        self.screen = [['.' for _ in range(self.px_min,self.px_max+1)] for _ in range(self.row_min,self.row_max+1)]
    
    def print_screen(self):
        for row in self.screen:
            print(''.join(row))

    def sprite_pos(self) -> list[int]:
        return [self.X + i for i in range(-1,2)if self.X + i >= self.px_min and self.X + i <= self.px_max]
    
    def px2draw(self) -> tuple[int,int]:
        return self.cycle//40,self.cycle%40
    
    def draw(self) -> None:
        y,x = self.px2draw()
        if x in self.sprite_pos():
            self.screen[y][x] = '#'

    def read_commands(self,commands: list[list[str]]) -> int:
        
        signal_strength_sum = 0

        for command in commands:
            self.cycle += 1
            signal_strength_sum += self.check_cycle()
            self.draw()
            if command[0] == 'noop':
                continue
            elif command[0] == 'addx':
                self.cycle += 1
                signal_strength_sum += self.check_cycle()
                self.X += int(command[1])
                self.draw()
            else:
                raise ValueError(command)
            
        self.cycle = 0
        self.X = 1
        self.next_check = 20

        return signal_strength_sum

    def check_cycle(self) -> int:
        if self.cycle == self.next_check:
            self.next_check += 40
            return self.cycle * self.X
        return 0

if __name__ == "__main__":

    with open(os.path.join(__location__, 'input10.txt')) as puzzle_input:
        commands = [line.strip().split() for line in puzzle_input.readlines()]
    
    com_sys = CommunicationSystem()
    print(com_sys.read_commands(commands))
    com_sys.print_screen()