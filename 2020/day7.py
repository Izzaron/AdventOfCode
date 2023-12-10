f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day7input.txt")

class Bag():
    def __init__(self,name,contains):
        self.name = name
        self.contains = contains
    
    def containsNr(self):
        return sum([number*(1+bags[name].containsNr()) for name,number in self.contains.items()])

bags = dict()

for line in f:
    containerStr,containsStr = line.strip().split("contain")
    containerName = containerStr.replace('bags','').replace('bag','').strip()

    containsList = containsStr.replace('.','').split(',')
    contains = dict()
    
    for c in containsList:
        if "no other bags" in c:
            continue

        number = int(c[1:2])
        
        name = c[3:].replace('bags','').replace('bag','').strip()

        contains[name] = number
    
    bag = Bag(containerName,contains)
    bags[bag.name] = bag

part = 2#input("part: ")

#Part 1
if part == 1:
    canContainBags = set()
    canContainBags.add("shiny gold")
    oldSize = len(canContainBags)
    while(True):
        for bag in bags.values():
            if bag.name in canContainBags:
                continue
            if canContainBags.intersection(set(bag.contains.keys())):
                canContainBags.add(bag.name)
        if oldSize != len(canContainBags):
            oldSize = len(canContainBags)
        else:
            break

    print(oldSize-1)

#Part 2
if part == 2:
    print(bags["shiny gold"].containsNr())