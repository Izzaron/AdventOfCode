import time

day23input = "476138259"

example = "389125467"

def play(cups,moves,printing,part):

    cups = [int(cup) for cup in cups]

    currentCup = cups[0]

    for move in range(moves):

        if printing:
            print(str(move+1)+':',','.join([str(c) for c in cups[0:10]]))

            print('current:',currentCup)

        pickUps = []
        for _ in range(3):
            pickUps.append( cups.pop( (cups.index(currentCup)+1) % len(cups) ) )

        if printing:
            print('pickup:',pickUps)

        i = 1
        while True:
            destinationCup = ((currentCup - 1 - i) % (len(cups)+3))+1
            # print('destination:',destinationCup)
            if destinationCup not in pickUps:
                break
            i += 1

        if printing:
            print('destination:',destinationCup)

        destIdx = cups.index(destinationCup)

        cups[destIdx+1:destIdx+1] = pickUps

        newCurrentCupIndex = (cups.index(currentCup)+1) % len(cups)

        currentCup = cups[newCurrentCupIndex]
        
        if printing:
            print()
    
    start = cups.index(1)

    if part == 1:
        ans = []
        for i in range(1,len(cups)):
            
            ans.append(cups[(i+start) % len(cups)])
        
        return ''.join([str(c) for c in ans])
    else:
        cup2 = cups[(start+1) % len(cups)]
        cup3 = cups[(start+2) % len(cups)]
        return cup2, cup3, cup2 * cup3

t0 = time.time()

print('final part 1:',play(day23input,100,False,1))

t1 = time.time()

#part 2

listLength = 1000000
nrMoves = 100

part2input = list(day23input) + [str(i) for i in range(len(day23input)+1,listLength+1)]
print('final part 2:',play(list(part2input),nrMoves,False,2))

t2 = time.time()

print("part 1: ",t1-t0)
print("part 2: ",t2-t1)
print("total: ",t2-t0)