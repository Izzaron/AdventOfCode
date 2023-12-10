import copy
from inspect import signature
from collections import defaultdict

class IntcodeProgram:

    def __init__(self,program,feedbackLoopMode=False,printOutput=False,printInstructions=False):
        self.programBlueprint = defaultdict(lambda:0,{i:program[i] for i in range(len(program))})
        self.program = copy.copy(self.programBlueprint)
        self.feedbackLoopMode = feedbackLoopMode
        self.instructionPointer = 0
        self.relativeBase = 0
        self.inputs = []
        self.outputs = []
        self.printOutput = printOutput
        self.printInstructions = printInstructions
        self.instructions = dict()
        self.instructions[1] = self.add
        self.instructions[2] = self.multiply
        self.instructions[3] = self.inputFunc
        self.instructions[4] = self.outputFunc
        self.instructions[5] = self.jumpIfTrue
        self.instructions[6] = self.jumpIfFalse
        self.instructions[7] = self.lessThan
        self.instructions[8] = self.equals
        self.instructions[9] = self.relativeBaseOffset
        self.instructions[99] = self.terminate
        self.isTerminated = False
    
    def add(self,instructionPointer,param1,param2,param3):
        
        self.program[param3] = self.program[param1] + self.program[param2]
        
        return True, instructionPointer

    def multiply(self,instructionPointer,param1,param2,param3):
        
        self.program[param3] = self.program[param1] * self.program[param2]
        
        return True, instructionPointer
    
    def inputFunc(self,instructionPointer,param1):
        
        if self.feedbackLoopMode and len(self.inputs) == 0:
            instructionPointer -= 2
            return False, instructionPointer

        self.program[param1] = self.inputs.pop(0)
        
        return True, instructionPointer
    
    def outputFunc(self,instructionPointer,param1):
        
        if self.printOutput:
            print('Output: {}'.format(self.program[param1]))
        self.outputs.append(self.program[param1])
        
        return True, instructionPointer
    
    def jumpIfTrue(self,instructionPointer,param1,param2):
        
        if self.program[param1] != 0:
            instructionPointer = self.program[param2] - 3
        
        return True, instructionPointer

    def jumpIfFalse(self,instructionPointer,param1,param2):
        
        if self.program[param1] == 0:
            instructionPointer = self.program[param2] - 3

        return True, instructionPointer

    def lessThan(self,instructionPointer,param1,param2,param3):
        
        if self.program[param1] < self.program[param2]:
            self.program[param3] = 1
        else:
            self.program[param3] = 0
        
        return True, instructionPointer

    def equals(self,instructionPointer,param1,param2,param3):
        
        if self.program[param1] == self.program[param2]:
            self.program[param3] = 1
        else:
            self.program[param3] = 0
        
        return True, instructionPointer
    
    def relativeBaseOffset(self,instructionPointer,param1):

        self.relativeBase += self.program[param1]

        return True, instructionPointer

    def terminate(self,instructionPointer):
        self.isTerminated = True
        return False, instructionPointer
    
    def getParameterMode(self,instructionPointer,argIdx):
        modes = str(self.program[instructionPointer])[:-2]
        if argIdx >= len(modes):
            return 0
        return int(modes[-(argIdx+1)])

    def readInstructionAt(self,instructionPointer):
        opcode = int(str(self.program[instructionPointer])[-2:])

        if opcode in self.instructions:
            function = self.instructions[opcode]

            nrOfParams = len(signature(function).parameters)
            args = [instructionPointer]
            for n in range(nrOfParams-1):
                mode = self.getParameterMode(instructionPointer,n)
                if mode == 0:
                    args.append(self.program[instructionPointer+n+1])
                elif mode == 1:
                    args.append(instructionPointer+n+1)
                elif mode == 2:
                    args.append(self.relativeBase + self.program[instructionPointer+n+1])
                else:
                    print('Unknown mode {} in instruction {}!'.format(mode,self.program[instructionPointer]))
                    raise SystemExit
            
            if self.printInstructions:
                print('Instruction: {} with arguments: {}'.format(self.program[instructionPointer],args))

            ans, instructionPointer = function(*args)

            instructionPointer += nrOfParams

            return ans, instructionPointer
        else:
            print('unknown instruction {}'.format(self.program[instructionPointer]))
            return False, instructionPointer
    
    def runTwo(self,noun,verb):

        self.program = copy.copy(self.programBlueprint)
        self.program[1] = noun
        self.program[2] = verb
        instructionPointer = 0
        
        returnCode = True

        while(returnCode):
            returnCode, instructionPointer = self.readInstructionAt(instructionPointer)

        return self.program[0]

    def run(self,*_args):

        self.inputs = list(_args)

        if self.feedbackLoopMode:
            instructionPointer = self.instructionPointer
        else:
            self.program = copy.copy(self.programBlueprint)
            instructionPointer = 0
        
        returnCode = True

        while(returnCode):
            returnCode, instructionPointer = self.readInstructionAt(instructionPointer)
        
        if self.feedbackLoopMode:
            self.instructionPointer = instructionPointer
        
        ret = copy.copy(self.outputs)

        self.outputs.clear()
        
        return ret