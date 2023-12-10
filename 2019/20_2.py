from pathfinding import Node
from coordinates import Coordinate
from collections import defaultdict
from holstcollections import ValueSortedDict

input_file = __file__.replace('_2.py','.txt')
test_file_1 = __file__.replace('_2.py','test1.txt')
test_file_2 = __file__.replace('_2.py','test2.txt')
test_file_3 = __file__.replace('_2.py','test3.txt')

class Karta:
    def __init__(self, file_path: str):
        self.karta      : list[list[Node]]      = []
        self.portals    : dict[str,list[Node]]  = defaultdict(lambda: list())
        self.inner      : dict[Node,Node]       = dict()
        self.outer      : dict[Node,Node]       = dict()

        with open(file_path) as puzzle_input:
            puzzle_lines = puzzle_input.readlines()
        
        self.create_nodes(puzzle_lines)
        self.detect_inner(puzzle_lines)
        self.aquaint()

    def create_nodes(self,puzzle_lines):
        for y,line in enumerate(puzzle_lines):
            row = []
            self.karta.append(row)
            for x,symbol in enumerate(line[:-1]):
                node = Node(symbol,Coordinate(x,y))
                row.append(node)

    def detect_inner(self,puzzle_lines):
        self.outer_left_top = None
        self.outer_right_top = None
        self.outer_width = None
        self.inner_left_top = None
        self.inner_right_top = None
        self.inner_left_bot = None
        for y,line in enumerate(puzzle_lines):
            for x,symbol in enumerate(line[:-1]):
                if self.outer_left_top == None and symbol == '#':
                    self.outer_left_top = Coordinate(x,y)
                if self.outer_left_top != None and self.outer_right_top == None and symbol == ' ':
                    self.outer_right_top = Coordinate(x,y)
                    self.outer_width = self.outer_right_top.x - self.outer_left_top.x
                if symbol == ' ' and self.inner_left_top == None and self.outer_left_top != None and self.outer_right_top != None and x>self.outer_left_top.x and x<self.outer_right_top.x:
                    self.inner_left_top = Coordinate(x,y)
                if self.inner_left_top != None and self.inner_right_top == None and symbol == '#':
                    self.inner_right_top = Coordinate(x-1,y)
                if self.inner_left_top != None and x == self.inner_left_top.x and self.inner_left_bot == None and symbol == '#':
                    self.inner_left_bot = Coordinate(x,y-1)
                    self.inner_right_bot = Coordinate(self.inner_right_top.x,self.inner_left_bot.y)
                    return

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
                pair0pos = portal_pair[0].position
                if pair0pos.x+1 >= self.inner_left_top.x and pair0pos.y+1 >= self.inner_left_top.y and pair0pos.x-1 <= self.inner_right_bot.x and pair0pos.y-1 <= self.inner_right_bot.y:
                    self.inner[portal_pair[0]] = portal_pair[1]
                    self.outer[portal_pair[1]] = portal_pair[0]
                else:
                    self.inner[portal_pair[1]] = portal_pair[0]
                    self.outer[portal_pair[0]] = portal_pair[1]

    def print(self, special: set[tuple[int,Node]], level: str):
        print('level',level)
        for row in self.karta:
            for node in row:
                if (level,node) in special:
                    print('■',end='')
                elif node in self.inner:
                    print('I',end='')
                elif node in self.outer:
                    print('O',end='')
                elif node is self.entrance:
                    print('E',end='')
                elif node is self.exit:
                    print('X',end='')
                else:
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

def distanceFromTo(startNode: tuple[int,Node], endNode: tuple[int,Node],karta: Karta) -> int:
    if startNode == endNode:
        return 0

    # have (level: int, Node) as key instead.
    nodeLibrary: ValueSortedDict[tuple[int,Node]] = ValueSortedDict([(startNode,0)])
    visitedNodes = set()

    currentLevel = 0
    parent_library: dict[Node,Node] = dict()
    
    while(nodeLibrary):

        currentNodeHash,currentDistance = nodeLibrary.pop(0)
        currentLevel,currentNode = currentNodeHash
        # karta.print(visitedNodes,currentLevel)
        # input()

        if currentNodeHash == endNode:
            node_path = []
            cn = currentNodeHash
            node_path.append(cn)
            while cn in parent_library:
                cn = parent_library[cn]
                node_path.append(cn)
            return currentDistance,list(reversed(node_path))

        visitedNodes.add(currentNodeHash)

        for nextNode,distanceToNextNode in currentNode.nearNodes.items():

            nextNodeHash = (currentLevel,nextNode)

            if nextNodeHash in visitedNodes:
                continue
            
            if nextNodeHash not in nodeLibrary or nodeLibrary[nextNodeHash] > currentDistance + distanceToNextNode:
                nodeLibrary[nextNodeHash] = currentDistance + distanceToNextNode
                parent_library[nextNodeHash] = currentNodeHash
        
        if currentNode in karta.inner:
            nextNodeHash = (currentLevel+1,karta.inner[currentNode])
            if nextNodeHash in visitedNodes:
                continue
            if nextNodeHash not in nodeLibrary or nodeLibrary[nextNodeHash] > currentDistance + distanceToNextNode:
                nodeLibrary[nextNodeHash] = currentDistance + distanceToNextNode
                parent_library[nextNodeHash] = currentNodeHash
        if currentLevel>0 and currentNode in karta.outer:
            nextNodeHash = (currentLevel-1,karta.outer[currentNode])
            if nextNodeHash in visitedNodes:
                continue
            if nextNodeHash not in nodeLibrary or nodeLibrary[nextNodeHash] > currentDistance + distanceToNextNode:
                nodeLibrary[nextNodeHash] = currentDistance + distanceToNextNode
                parent_library[nextNodeHash] = currentNodeHash

    return None

def main():
    karta = Karta(input_file)
    # karta.print()
    d,p = distanceFromTo((0,karta.entrance),(0,karta.exit),karta)
    # current_level = 0
    # steps_since_last = 0
    # for n in p:
    #     if n[0] != current_level:
    #         current_level = n[0]
    #         print('walked',steps_since_last)
    #         print('going to',n[0])
    #         steps_since_last = 0
    #     else:
    #         steps_since_last += 1
    # print('walked',steps_since_last)
    # print(len(p))
    # specials = set()
    # karta.print(specials,0)
    # for n in p:
    #     input()
    #     specials.add(n)
    #     karta.print(specials,n[0])
    print(d)

if __name__ == '__main__':
    main()

# 3836 too low