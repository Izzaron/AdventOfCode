import os
from pathfinding import Node
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class NodeMap:
    def __init__(self,karta: list[list[str]]) -> None:
        for j,row in enumerate(karta):
            for i,square in enumerate(row):
                if square == 'S':
                    self.start = (i,j)
                    karta[j][i] = 'a'
                if square == 'E':
                    self.end = (i,j)
                    karta[j][i] = 'z'
        self.nodes = [[Node(square) for square in row] for row in karta]
        self.start = self.nodes[self.start[1]][self.start[0]]
        self.end = self.nodes[self.end[1]][self.end[0]]
        self.height = len(self.nodes)
        self.width = len(self.nodes[0])
        self.connect_nodes()

    def at(self,x,y):
        if x<0 or y<0:
            return None
        try:
            return self.nodes[y][x]
        except IndexError:
            return None

    def print(self):
        for row in self.nodes:
            for node in row:
                print(node.nodeType,end='')
            print()

    def connect_nodes(self):
        for j,row in enumerate(self.nodes):
            for i,node in enumerate(row):
                neighbours = [self.at(i+dir[0],j+dir[1]) for dir in [(0,1),(0,-1),(1,0),(-1,0)] if self.at(i+dir[0],j+dir[1])]
                for neighbour in neighbours:
                    if ord(neighbour.nodeType) - ord(node.nodeType) <= 1:
                        node.addNearNode(neighbour,1)

    def iter(self):
        return (node for row in self.nodes for node in row)

if __name__ == "__main__":

    with open(os.path.join(__location__, 'input12.txt')) as puzzle_input:

        karta = [list(line.strip()) for line in puzzle_input]

    node_map = NodeMap(karta)
    # node_map.print()
    print(node_map.start.getShortestDistanceTo(node_map.end))
    distances = [node.getShortestDistanceTo(node_map.end) for node in node_map.iter() if node.nodeType == 'a']
    distances = [node for node in distances if node]
    print(min(distances))