import copy
from intcodeprogram import IntcodeProgram
from coordinates import Coordinate, Direction
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input17.txt' )

testMap = '''..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^..'''

markerToDirection = {
    '^': 90,
    'v': 270,
    '<': 180,
    '>': 0
}

class VacuumRobot:
    def __init__(self,software,feedbackLoopMode=False,part=1):
        self.computer = IntcodeProgram(software,feedbackLoopMode)
        self.map = dict()
        self.score = None
        self.part = part
        self.position = None
        self.direction = None
    
    def run(self,testMap=None,programInput=[]):

        #load map
        if testMap:
            output = list(testMap)
        else:
            rawOutput = self.computer.run(*programInput)
            if self.part == 1:
                rawOutput.pop()
            elif self.part == 2:
                self.score = rawOutput.pop()
            output = map(chr,rawOutput)

        #format map
        # row = []
        # for char in output:
        #     if char == '\n':
        #         self.map.append(row)
        #         row = []
        #     else:
        #         row.append(char)

        row = dict()
        x = 0
        y = 0
        for char in output:
            if char == '\n':
                self.map[y] = row
                y -= 1
                x = 0
                row = dict()
            else:
                row[x] = char
                x += 1
        
        self.position,self.direction = self.determinePositionAndDirection()
    
    def determinePositionAndDirection(self):
        markers = ['^', 'v', '<','>','X']
        for y,row in self.map.items():
            for x,point in row.items():
                if point in markers:
                    return Coordinate(x,y),Direction(markerToDirection[point])

    def print(self):
        for row in self.map.values():
            for char in row.values():
                print(char,end='')
            print()
        if self.score:
            print("Dust collected:",self.score)
            
    def countIntersections(self):
        tot = 0
        for y,row in self.map.items():
            for x,point in row.items():
                if point == '#' and self.isIntersection(x,y):
                    tot += abs(x)*abs(y)
        return tot

    def isScaffold(self,x,y=None):
        scaffold = markers = ['^', 'v', '<','>','#']
        if y == None:
            y = x.y
            x = x.x
        try:
            return self.map[y][x] in scaffold
        except KeyError:
            return False
    
    def isIntersection(self,x,y):
        for d in [-1,1]:
            if not self.isScaffold(x, y+d):
                return False
            if not self.isScaffold(x+d, y):
                return False
        return True

    def walk(self):
        if self.isScaffold(self.position.getStepInDirection(1, self.direction)):
            steps = 0
            while self.isScaffold(self.position.getStepInDirection(1, self.direction)):
                self.step()
                steps += 1
            return str(steps)
        elif self.isScaffold(self.position.getStepInDirection(1, self.direction+90)):
            self.direction += 90
            return 'L'
        elif self.isScaffold(self.position.getStepInDirection(1, self.direction-90)):
            self.direction -= 90
            return 'R'
        else:
            return False
    
    def step(self,steps=1):
        self.position.stepInDirection(steps, self.direction)

def part1():
    puzzleInput = open(filename)
    sugisSoftware = [int(i) for i in puzzleInput.read().split(',')]

    sugis = VacuumRobot(sugisSoftware)
    sugis.run()
    sugis.print()
    print("Intersection score:",sugis.countIntersections())

def part2():
    # Determine path

    puzzleInput = open(filename)
    sugisSoftware = [int(i) for i in puzzleInput.read().split(',')]

    sugis = VacuumRobot(sugisSoftware)
    sugis.run()
    sugis.print()
    
    # sugis.direction += 90 #L
    # sugis.step(12) #12
    # sugis.direction += 90 #L
    # sugis.step(12) #12
    # sugis.direction -= 90 #R
    # sugis.step(4) #4
    # sugis.direction -= 90 #R
    # sugis.step(4) #4
    
    instruction = True
    instructions = []
    while True:
        instruction = sugis.walk()
        if not instruction:
            break
        instructions.append(instruction)
    print(''.join(instructions))
    print(len(instructions))
    # L12L12R4 R10R6R4R4 L12L12R4 R6L12L12 R10R6R4R4 L12L12R4 R10R6R4R4 R6L12L12 R6L12L12 R10R6R4R4
    # A C A B C A C B B C
    # A L12L12R4
    # B R6L12L12
    # C R10R6R4R4


    # the whole path is now determined and stored in 'instructions'
    # what is left to do is to sectionize 'instructions' into groups A, B and C


    

    #Sectionize path
    sugisSoftware[0] = 2

    mainRoutine =   "A,C,A,B,C,A,C,B,B,C"
    functionA =     "L,12,L,12,R,4"
    functionB =     "R,6,L,12,L,12"
    functionC =     "R,10,R,6,R,4,R,4"
    videoFeed =     "n"
    programInput = map(ord,mainRoutine+'\n'+functionA+'\n'+functionB+'\n'+functionC+'\n'+videoFeed+'\n')

    sugis = VacuumRobot(sugisSoftware,part=2)
    sugis.run(programInput=programInput)
    sugis.print()

if __name__ == '__main__':
    # part1()
    part2()