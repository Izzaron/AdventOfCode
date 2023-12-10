import getch
import random
from intcodeprogram import IntcodeProgram

class GraphicsCard:

    def __init__(self,inputSignal):
        self.library = {
            0: ' ',
            1: '■',
            2: '□',
            3: '-',
            4: 'o',
        }
        self.score = 0
        cleanedInputSignal = [inputSignal[x:x+3] for x in range(0, len(inputSignal), 3)]
        self.xMax = max([x[0] for x in cleanedInputSignal])
        self.yMax = max([x[1] for x in cleanedInputSignal])
        self.screen = [['X' for _ in range(self.xMax + 1)] for _ in range(self.yMax + 1)]

        self.paddleX = [x for x in cleanedInputSignal if x[2] == 3][0][0]
        self.ballX = [x for x in cleanedInputSignal if x[2] == 4][0][0]

        self.readInput(inputSignal)

        # for instruction in cleanedInputSignal:
        #     if instruction[0] == -1 and instruction[1] == 0:
        #         self.score = instruction[2]
        #         continue
        #     self.screen[instruction[1]][instruction[0]] = self.library[instruction[2]]

    def readInput(self,inputSignal):

        cleanedInputSignal = [inputSignal[x:x+100] for x in range(0, len(inputSignal), 3)]

        paddle = [x for x in cleanedInputSignal if x[2] == 3]
        if len(paddle) > 0:
            self.paddleX = paddle[0][0]
        ball = [x for x in cleanedInputSignal if x[2] == 4]
        if len(ball) > 0:
            self.ballX = ball[0][0]

        for instruction in cleanedInputSignal:
            if instruction[0] == -1 and instruction[1] == 0:
                self.score = instruction[2]
                continue
            self.screen[instruction[1]][instruction[0]] = self.library[instruction[2]]
        
    
    def print(self):
        print(''.join(['S' for _ in range(self.xMax - len(str(self.score)) )]),self.score)
        for row in self.screen:
            print(''.join(row))

def main():
    puzzleInput = open("input13.txt")
    arcadeCabinetSoftware = [int(i) for i in puzzleInput.read().split(',')]

    arcadeCabinetSoftware[0] = 2

    arcadeCabinet = IntcodeProgram(arcadeCabinetSoftware,feedbackLoopMode=True)

    screenInput = arcadeCabinet.run()

    gc = GraphicsCard(screenInput)

    mode = input('mode? (manual,random,auto): ')

    gc.print()

    inputDict = {
        'a': -1,
        's': 0,
        'd': 1,
    }

    while(True):

        if mode == 'manual':
            joysticInput = getch.getch()
            translatedInput = inputDict[joysticInput]
        elif mode == 'random':
            translatedInput = random.randint(-1,1)
        elif mode == 'auto':
            if gc.ballX == gc.paddleX:
                translatedInput = 0
            elif gc.ballX > gc.paddleX:
                translatedInput = 1
            elif gc.ballX < gc.paddleX:
                translatedInput = -1

        screenInput = arcadeCabinet.run(translatedInput)

        gc.readInput(screenInput)

        gc.print()

        if arcadeCabinet.isTerminated:
            print('score: ',gc.score)
            break

    # print(len([x for x in gc.inputSignal if x[2] == 2]))

    

if __name__ == '__main__':
    main()