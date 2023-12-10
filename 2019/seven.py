from intcodeprogram import IntcodeProgram
import itertools

def main():
    puzzleInput = open("input7.txt")
    ampControllerSoftware = [int(i) for i in puzzleInput.read().split(',')]

    #part 1

    permutations = list(itertools.permutations([0, 1, 2, 3, 4]))

    icp = IntcodeProgram(ampControllerSoftware)
    answers = dict()
    for phaseSetting in permutations:
        ampInput = 0
        for ps in phaseSetting:
            ampInput = icp.run(ps,ampInput)[0]
        answers[ampInput] = phaseSetting
    
    maxAmpOutput = max(answers)
    print(maxAmpOutput)
    print(answers[maxAmpOutput])

    #part 2

    permutations = list(itertools.permutations([5, 6, 7, 8, 9]))
    
    answers = dict()
    for phaseSetting in permutations:
    
        # print('Amp A')
        ampA = IntcodeProgram(ampControllerSoftware,True)
        ampA.run(phaseSetting[0])
        # print('Amp B')
        ampB = IntcodeProgram(ampControllerSoftware,True)
        ampB.run(phaseSetting[1])
        # print('Amp C')
        ampC = IntcodeProgram(ampControllerSoftware,True)
        ampC.run(phaseSetting[2])
        # print('Amp D')
        ampD = IntcodeProgram(ampControllerSoftware,True)
        ampD.run(phaseSetting[3])
        # print('Amp E')
        ampE = IntcodeProgram(ampControllerSoftware,True)
        ampE.run(phaseSetting[4])

        ampInput = 0
        while(True):
            
            # print('Amp A')
            ampInput = ampA.run(ampInput)[0]
            
            # print('Amp B')
            ampInput = ampB.run(ampInput)[0]
            
            # print('Amp C')
            ampInput = ampC.run(ampInput)[0]
            
            # print('Amp D')
            ampInput = ampD.run(ampInput)[0]
            
            # print('Amp E')
            ampInput = ampE.run(ampInput)[0]
            
            stati = [ampA.isTerminated,ampB.isTerminated,ampC.isTerminated,ampD.isTerminated,ampE.isTerminated]
            if any(stati) and not all(stati):
                print('Some but not all amplifiers were terminated')
                raise SystemExit
            elif all(stati):
                # print('All amplifiers terminated simultaneously')
                # print(ampInput)
                break


        answers[ampInput] = phaseSetting
    
    maxAmpOutput = max(answers)
    print(maxAmpOutput)
    print(answers[maxAmpOutput])

if __name__ == '__main__':
    main()