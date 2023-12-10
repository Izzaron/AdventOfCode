from pathfinding import Node
from coordinates import Coordinate
from collections import defaultdict
from holstcollections import ValueSortedDict

input_file = __file__.replace('.py','.txt')
test_file_1 = __file__.replace('.py','test1.txt')
test_file_2 = __file__.replace('.py','test2.txt')

class Karta:
    def __init__(self, file_path: str):
        self.karta      : list[list[Node]]      = []
        self.portals    : dict[str,list[Node]]  = defaultdict(lambda: list())

        with open(file_path) as puzzle_input:
            for y,line in enumerate(puzzle_input):
                row = []
                self.karta.append(row)
                for x,symbol in enumerate(line[:-1]):
                    node = Node(symbol,Coordinate(x,y))
                    row.append(node)

        self.aquaint()

    def aquaint(self):
        for node in self.iterator():
            if node.name != '.':
                continue
            for neighbour in self.getSurroundings(node.position):
                if neighbour.name == '.':
                    node.addNearNode(neighbour,1)
                else:
                    dr = node.position.direction_to(neighbour.position)
                    nei_nei = self.at( neighbour.position.getCoordinateInDirection(dr) )
                    neihs = [neighbour,nei_nei]
                    if dr.is_horizontal():
                        self.portals[''.join(k.name for k in sorted(neihs,key=lambda n: n.position.x))].append(node)
                    elif dr.is_vertical():
                        self.portals[''.join(k.name for k in sorted(neihs,key=lambda n: n.position.y))].append(node)
                    else:
                        raise ValueError()
        
        for key,portal_pair in self.portals.items():
            if key == 'AA':
                self.entrance = portal_pair[0]
            elif key == 'ZZ':
                self.exit = portal_pair[0]
            else:
                portal_pair[0].addNearNode(portal_pair[1])
                portal_pair[1].addNearNode(portal_pair[0])

    def print(self):
        for row in self.karta:
            for node in row:
                print(node.name,end='')
            print()
    
    def at(self,position: Coordinate):
        try:
            node = self.karta[position.y][position.x]
            if node.name == ' ' or node.name == '#':
                return False
            return node
        except IndexError:
            return False
    
    def getSurroundings(self,position: Coordinate) -> list[Node]:
        surroundings = []
        for step in [Coordinate(-1,0),Coordinate(1,0),Coordinate(0,-1),Coordinate(0,1)]:
            coordinate = position + step
            node = self.at(coordinate)
            if node:
                surroundings.append(node)
        return surroundings

    def iterator(self):
        return (item for it in self.karta for item in it)

def distanceFromTo(startNode: Node, endNode: Node, excluding: list[Node] = [], allow_shortcuts: bool = True) -> int:
    if startNode == endNode:
        return 0
    if allow_shortcuts and endNode in startNode.shortcuts:
        return startNode.shortcuts[endNode]
    nodeLibrary: ValueSortedDict[Node] = ValueSortedDict([(startNode,0)])
    visitedNodes = []
    
    while(nodeLibrary):

        currentNode,currentDistance = nodeLibrary.pop(0)

        if currentNode == endNode:
            startNode.shortcuts[endNode] = currentDistance
            return currentDistance

        visitedNodes.append(currentNode)

        for nextNode,distanceToNextNode in currentNode.nearNodes.items():

            if nextNode in visitedNodes:
                continue
                
            if nextNode in excluding:
                continue
            
            if nextNode not in nodeLibrary or nodeLibrary[nextNode] > currentDistance + distanceToNextNode:
                nodeLibrary[nextNode] = currentDistance + distanceToNextNode

    return None

def main():
    karta = Karta(input_file)

    print(distanceFromTo(karta.entrance,karta.exit))

if __name__ == '__main__':
    main()