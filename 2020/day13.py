f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/Day13input.txt")

lines = [l for l in f]

earliest = int(lines[0])

problemNr = 1

busLines = [int(l) for l in lines[problemNr].strip().split(',') if l.isdigit()]

allBusLines = [l for l in lines[problemNr].strip().split(',')]

# smallestWait = earliest
# smallestLine = 0
# for bl in busLines:
#     k = 1
#     while(k*bl <= earliest):
#         k += 1
#     if k*bl-earliest < smallestWait:
#         smallestWait = k*bl-earliest
#         smallestLine = bl

# print(smallestLine,smallestWait,smallestLine*smallestWait)

#part 2

bli = {int(k):v for v,k in enumerate(allBusLines) if k.isdigit()}

for bab in busLines:
    print(bab,bli[bab])

t = 0
step = 1
willPrint = 10

for bl in busLines:
    while(True):
        
        t += step

        if t > willPrint:
            print(t,step,bl,bli[bl])
            willPrint *= 10
        
        if (t+bli[bl])%bl == 0:
            break
    step *= bl

print(t)

#27690454827000 too low
1000000001165965341696
123456789012345678901234567890