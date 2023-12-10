from intcodeprogram import IntcodeProgram

def main():
    puzzleInput = open(r"b:\Dropbox\Projects\AdventOfCode\2019\input9.txt")
    listan = [int(i) for i in puzzleInput.read().split(',')]

    icp = IntcodeProgram(listan)
    print(icp.run(2))

if __name__ == '__main__':
    main()