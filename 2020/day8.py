import copy

f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day8input.txt")

class Processor:
    
    @staticmethod
    def convertFileToProgram(file):
        return [ ( line.strip().split(' ')[0] , int(line.strip().split(' ')[1])) for line in f]

    def __init__(self,program):
        self.line = 0
        self.accumulator = 0
        self.program = program
        self.linesRun = set()

    def run(self):
        while(True):
            if self.line in self.linesRun:
                return False
            if self.line == len(self.program):
                return True
            self.linesRun.add(self.line)
            self.compute(self.program[self.line])
    
    def compute(self,instruction):
        if instruction[0] == "jmp":
            self.line += instruction[1]
        elif instruction[0] == "acc":
            self.accumulator += instruction[1]
            self.line += 1
        elif instruction[0] == "nop":
            self.line += 1
        else:
            print("Found undifined instruction \"{}\"!".format(instruction[0]))
            exit()

program = Processor.convertFileToProgram(f)

#Part 1
# handheldGameConsole = Processor(program)
# handheldGameConsole.run()
# print(handheldGameConsole.accumulator)

#Part 2
for line in range(len(program)):
    if program[line][0] == "acc":
        continue

    fixedProgram = copy.deepcopy(program)

    if program[line][0] == "nop":
        fixedProgram[line] = ("jmp",program[line][1])
    elif program[line][0] == "jmp":
        fixedProgram[line] = ("nop",program[line][1])

    handheldGameConsole = Processor(fixedProgram)
    if handheldGameConsole.run():
        print(handheldGameConsole.accumulator)
        break
