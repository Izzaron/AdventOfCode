import time

class Node:

    #Define instance members
    def __init__(self,jolt):
        self.jolt = jolt
        self.children = []
        self.waysToGetHere = 0

    #Define recursive function to calculate number of combinations that can lead to this node
    def getWaysToGetHere(self):

        #If the value is already calculated, return the stored value
        if self.waysToGetHere != 0:
            return self.waysToGetHere

        #If the node has children the combination of ways to this node is the sum of the childrens
        if self.children:
            self.waysToGetHere = sum([c.getWaysToGetHere() for c in self.children])
        
        #If the nod has no children (is the top node) return 1
        else:
            self.waysToGetHere = 1
        
        return self.waysToGetHere

#Start clock
start = time.time()

#Open input
f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/Day10input.txt")

#Put input in list
jolts = [int(i) for i in f]

#Sort input and add edge nodes (0 and last+3)
sortedJolts = sorted(jolts)
sortedJolts.insert(0,0)
sortedJolts.append(sortedJolts[-1]+3)

#Create node objects from list
joltNodes = []
for jolt in sortedJolts:
    joltNode = Node(jolt)
    joltNodes.append(joltNode)

#Add "children" nodes to node list
for i,joltNode in enumerate(joltNodes):
    if i == len(joltNodes) - 1:
        break
    for joltChild in joltNodes[(i+1):]:
        if (joltChild.jolt - joltNode.jolt) <= 3:
            joltNode.children.append(joltChild)

#Get answer
print(joltNodes[0].getWaysToGetHere())

end = time.time()
print(end - start)

#part 1
oneDiff = 0
threeDiff = 0
for i,jolt in enumerate(sortedJolts[:-1]):
    diff = sortedJolts[i+1] - jolt
    if diff  == 1:
        oneDiff += 1
    elif diff  == 3:
        threeDiff += 1

print(oneDiff*threeDiff)