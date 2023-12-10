from intcodeprogram import IntcodeProgram

def main():
    puzzleInput = open("input5.txt")
    listan = [int(i) for i in puzzleInput.read().split(',')]

    icp = IntcodeProgram(listan)
    print(icp.run(1))
    print(icp.run(5))

    puzzleInput = open("input2.txt")
    listan = [int(i) for i in puzzleInput.read().split(',')]

    icp = IntcodeProgram(listan)
    for noun in range(100):
        for verb in range(100):
            if icp.runTwo(noun,verb) == 19690720:
                print(100*noun + verb)
                return

if __name__ == '__main__':
    main()