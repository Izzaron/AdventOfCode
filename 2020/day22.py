from copy import copy
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'day' + str(22) + 'input.txt' )
f = open(filename)

deck1 = []
deck2 = []
for line in f:
    if 'Player 1:' in line:
        while True:
            line = f.readline()
            if line == '\n':
                f.readline()
                break
            deck1.append(int(line))
    else:
        deck2.append(int(line))

def calculateScore(deck):
    return sum([a*b for a,b in zip(deck,range(len(deck),0,-1))])

def play(deck1,deck2):

    while True:
        if len(deck1) == 0:
            return calculateScore(deck2)
        elif len(deck2) == 0:
            return calculateScore(deck1)
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if card1 > card2:
            deck1 += [card1,card2]
        else:
            deck2 += [card2,card1]

# print(play(deck1,deck2))

#part 2

def playRecursive(deck1,deck2,depth):
    passedGames1 = []
    passedGames2 = []
    while True:
        #finfinite loop rule
        serialize1 = tuple(deck1)
        serialize2 = tuple(deck2)
        if serialize1 in passedGames1 or serialize2 in passedGames2:
            return calculateScore(deck1)
        else:
            passedGames1.append(serialize1)
            passedGames2.append(serialize2)
        
        #draw cards
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        #recursive rule
        if len(deck1) >= card1 and len(deck2) >= card2:
            if playRecursive(copy(deck1[0:card1]),copy(deck2[0:card2]),depth+1) > 0:
                deck1 += [card1,card2]
            else:
                deck2 += [card2,card1]
        #fall-back regular rule
        else:
            if card1 > card2:
                deck1 += [card1,card2]
            else:
                deck2 += [card2,card1]
        
        #regular rule
        if len(deck1) == 0:
            return -calculateScore(deck2)
        if len(deck2) == 0:
            return calculateScore(deck1)

print(playRecursive(deck1,deck2,0))