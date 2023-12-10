import getch
import copy
import os
import random

from intcodeprogram import IntcodeProgram
from coordinates import Coordinate
from pathfinding import Node

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

transCord = {
    1: Coordinate(0,-1),
    2: Coordinate(0,1),
    3: Coordinate(-1,0),
    4: Coordinate(1,0)
}

reverseDirection = {
    1: 2,
    2: 1,
    3: 4,
    4: 3,
}

class DroidRemoteControl:
    def __init__(self,repairDroidRemoteControlSoftware):
        self.board = []
        self.items = dict()
        self.minX = 0
        self.maxX = 1
        self.minY = 0
        self.maxY = 1
        self.droidPos = Coordinate(0,0)
        self.oxygenSystemFound = False
        self.oxygenSystemPos = None
        self.repairDroidRemote = IntcodeProgram(repairDroidRemoteControlSoftware,feedbackLoopMode=True)
        self.currentNode = Node('start')
        self.nodes = {Coordinate(0,0): self.currentNode}
        self.stepsSinceLastNode = 0
    
    def autoMove(self):
        self.explore()

        self.recordNode()

        self.stepsSinceLastNode += 1
        
        openPathsInVicinity = [direction for direction in range(1,5) if self.items[(self.droidPos + transCord[direction])] == ':']
        exploredPathsInVicinity = [direction for direction in range(1,5) if self.items[(self.droidPos + transCord[direction])] == '.']
        
        if len(openPathsInVicinity) == 0 and len(exploredPathsInVicinity) == 0:
            return 0
        elif len(openPathsInVicinity) == 1 and len(exploredPathsInVicinity) == 0:
            self.items[self.droidPos] = '□'
            return openPathsInVicinity[0]
        elif len(openPathsInVicinity) == 0 and len(exploredPathsInVicinity) == 1:
            self.items[self.droidPos] = '□'
            return exploredPathsInVicinity[0]
        
        return openPathsInVicinity[0]
    
    def explore(self):
        for remoteCommand in range(1,5):
            response = self.repairDroidRemote.run(remoteCommand)[0]

            if response == 0:
                self.items[(self.droidPos + transCord[remoteCommand])] = '■'
            elif response == 1:
                if (self.droidPos + transCord[remoteCommand]) not in self.items:
                    self.items[(self.droidPos + transCord[remoteCommand])] = ':'
                self.repairDroidRemote.run(reverseDirection[remoteCommand])[0]
            elif response == 2:
                if (self.droidPos + transCord[remoteCommand]) not in self.items:
                    self.items[(self.droidPos + transCord[remoteCommand])] = ':'
                self.repairDroidRemote.run(reverseDirection[remoteCommand])[0]
                self.oxygenSystemPos = copy.copy(self.droidPos + transCord[remoteCommand])
                self.oxygenSystemFound = True
    
    def recordNode(self):
        
        wallsInVicinity = [direction for direction in range(1,5) if self.items[(self.droidPos + transCord[direction])] == '■']

        if self.oxygenSystemFound and self.droidPos == self.oxygenSystemPos:
            nodeType = 'end'
        elif len(wallsInVicinity) < 2:
            nodeType = 'crossing'
        else:
            return
        
        if self.droidPos in self.nodes:
            newNode = self.nodes[self.droidPos]
        else:
            newNode = Node(nodeType)
            self.nodes[self.droidPos] = newNode
        
        self.currentNode.addNearNode(newNode,self.stepsSinceLastNode)
        newNode.addNearNode(self.currentNode,self.stepsSinceLastNode)

        self.currentNode = newNode

        self.stepsSinceLastNode = 0

    def readInput(self,remoteCommand):
        response = self.repairDroidRemote.run(remoteCommand)[0]
        if response == 0:
            self.items[(self.droidPos + transCord[remoteCommand])] = '■'
        elif response == 1:
            if self.droidPos not in self.items or self.items[self.droidPos] == ':':
                self.items[self.droidPos] = '.'
            self.droidPos += transCord[remoteCommand]
        elif response == 2:
            if self.droidPos not in self.items or self.items[self.droidPos] == ':':
                self.items[self.droidPos] = '.'
            self.droidPos += transCord[remoteCommand]
            self.oxygenSystemPos = copy.copy(self.droidPos)
            self.oxygenSystemFound = True
        return response

    def print(self):
        itemsWithDroid = copy.copy(self.items)
        itemsWithDroid[Coordinate(0,0)] = 'S'
        itemsWithDroid[self.droidPos] = 'D'
        if self.oxygenSystemFound:
            itemsWithDroid[self.oxygenSystemPos] = 'F'
        self.minX = min([coord.x for coord,_ in itemsWithDroid.items()])
        self.maxX = max([coord.x for coord,_ in itemsWithDroid.items()])
        self.minY = min([coord.y for coord,_ in itemsWithDroid.items()])
        self.maxY = max([coord.y for coord,_ in itemsWithDroid.items()])
        diffX = -1 * self.minX
        diffY = -1 * self.minY
        self.board = [[' ' for _ in range(diffX + self.maxX + 1)] for _ in range(diffY + self.maxY + 1)]
        for coord,item in itemsWithDroid.items():
            self.board[diffY + coord.y][diffX + coord.x] = item
        
        os.system('clear')
        for row in self.board:
            print(' '.join(row))

def main():
    puzzleInput = open(os.path.join(__location__, "input15.txt"))
    repairDroidRemoteControlSoftware = [int(i) for i in puzzleInput.read().split(',')]

    inputDict = {
        'w': 1,
        'a': 3,
        's': 2,
        'd': 4,
    }

    mode = input('mode? (manual,auto)')
    printMode = input('print? y/n')

    drc = DroidRemoteControl(repairDroidRemoteControlSoftware)
    if printMode == 'y':
        drc.print()

    while(True):
        if mode == 'manual':
            joysticInput = getch.getch()
            if joysticInput == 'r':
                remoteCommand = random.randint(1,4)
            elif joysticInput == 'e':
                drc.explore()
                drc.print()
                continue
            elif joysticInput == 't':
                remoteCommand = drc.autoMove()
            else:
                if not joysticInput in inputDict:
                    continue
                remoteCommand = inputDict[joysticInput]
        elif mode == 'auto':
            remoteCommand = drc.autoMove()
        
        if remoteCommand == 0:
            drc.print()
            break
        drc.readInput(remoteCommand)
        if printMode == 'y':
            drc.print()
    

    #find shortest path
    
    startNode = [node for node in drc.nodes.values() if node.nodeType == 'start'].pop()

    endNode = [node for node in drc.nodes.values() if node.nodeType == 'end'].pop()

    shortestDistance = startNode.distanceTo(endNode)

    print(shortestDistance)

    # part 2

    floodStart = drc.oxygenSystemPos

    drc.items[floodStart] = '■'

    floodEdges = [floodStart]

    floodTime = 0

    while(True):

        newFloodEdges = []

        for floodEdge in floodEdges:

            for floodDirection in range(1,5):

                nextFloodCoordinate = floodEdge + transCord[floodDirection]

                if drc.items[nextFloodCoordinate] != '■':
                    newFloodEdges.append(nextFloodCoordinate)
                    drc.items[nextFloodCoordinate] = '■'
        
        if len(newFloodEdges) == 0:
            break
        
        floodEdges = copy.copy(newFloodEdges)

        floodTime += 1

        drc.print()
    
    print('Flood time: ',floodTime)
    # not 361 360 362 359 358
    

if __name__ == '__main__':
    main()