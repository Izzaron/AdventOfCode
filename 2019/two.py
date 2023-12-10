import math,copy
from intcodeprogram import IntcodeProgram

def main():
    input = open("input2.txt")
    listan = [int(i) for i in input.read().split(',')]

    for noun in range(100):
        for verb in range(100):
            icp = IntcodeProgram(listan)
            if icp.runTwo(noun,verb) == 19690720:
                
                print(100*noun + verb)
                return

if __name__ == '__main__':
    main()