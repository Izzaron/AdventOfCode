import time

day23input = "476138259"

example = "389125467"

class Cup:
    def __init__(self,val):
        self.value = val
        self.next = None

def play(cups,moves,printing,part):

    cupDict = dict()

    firstCup = Cup(int(cups[0]))
    cupDict[firstCup.value] = firstCup
    prevCup = firstCup
    for cup in cups[1:]:
        nextCup = Cup(int(cup))

        cupDict[nextCup.value] = nextCup

        prevCup.next = nextCup
        prevCup = nextCup
    nextCup.next = firstCup

    currentCup = firstCup

    for move in range(moves):

#        if printing:
#            print(str(move+1)+':',','.join([str(c) for c in cups[0:10]]))
#
#            print('current:',currentCup)

        pickUps = []
        pickUps.append( currentCup.next )
        pickUps.append( currentCup.next.next )
        pickUps.append( currentCup.next.next.next )

        currentCup.next = pickUps[-1].next
        pickUps[-1].next = None

#        if printing:
#            print('pickup:',pickUps)

        i = 1
        while True:
            destinationCup = cupDict[((currentCup.value - 1 - i) % (len(cups)))+1]
            # print('destination:',destinationCup)
            if destinationCup not in pickUps:
                break
            i += 1

#            if printing:
#                print('destination:',destinationCup)

        pickUps[-1].next = destinationCup.next
        destinationCup.next = pickUps[0]

        currentCup = currentCup.next
        
#            if printing:
#               print()
    
    startCup = cupDict[1]

    nextCup = startCup.next
    if part == 1:
        ans = []
        while nextCup != startCup:
            ans.append(nextCup.value)
            nextCup = nextCup.next
        
        return ''.join([str(c) for c in ans])
    else:
        cup2 = startCup.next.value
        cup3 = startCup.next.next.value
        return cup2, cup3, cup2 * cup3

t0 = time.time()

print('final part 1:',play(day23input,100,False,1))

t1 = time.time()

#part 2

listLength = 1000000
nrMoves = 10000000

part2input = list(day23input) + [str(i) for i in range(len(day23input)+1,listLength+1)]
print('final part 2:',play(list(part2input),nrMoves,False,2))

t2 = time.time()

print("part 1: ",t1-t0)
print("part 2: ",t2-t1)
print("total: ",t2-t0)