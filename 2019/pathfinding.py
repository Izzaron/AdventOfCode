from holstcollections import ValueSortedDict
from coordinates import Coordinate
class Node:
    def __init__(self,name: str, position: Coordinate = None):
        self.nearNodes:     dict['Node'] = dict()
        self.shortcuts:     dict['Node'] = dict()
        self.name:          str          = name
        self.position:      Coordinate   = position
    
    def __str__(self):
        return 'Node<{}>: {}'.format(self.name,self.nearNodes)
    
    def __repr__(self):
        return 'Node<{}>'.format(self.name)

    def addNearNode(self,nearNode: 'Node',distance: int = 1):
        self.nearNodes[nearNode] = distance
    
    def pathsTo(self, to_nodes: list['Node']) -> list[list['Node']]:
        return self.pathsFromTo(self,to_nodes)
    
    def distanceTo(self, endNode: 'Node', excluding: list['Node'] = [], allow_shortcuts: bool = True) -> int:
        return self.distanceFromTo(self,endNode,excluding,allow_shortcuts)

    @staticmethod
    def distanceFromTo(startNode: 'Node', endNode: 'Node', excluding: list['Node'] = [], allow_shortcuts: bool = True) -> int:
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

    @staticmethod
    def pathsFromTo(from_node: 'Node', to_nodes: list['Node']) -> list[list['Node']]:
        nodeLibrary:    ValueSortedDict[Node]   = ValueSortedDict([(from_node,0)])
        visitedNodes:   set[Node]               = set()
        parent_library: dict[Node,Node]         = dict()
        paths:          list[list[Node]]        = list()
        
        while(nodeLibrary):

            currentNode,currentDistance = nodeLibrary.pop(0)
            if currentNode in to_nodes:
                child_node = currentNode
                node_path = []
                while(True):
                    node_path.append(child_node)
                    if child_node in parent_library:
                        child_node = parent_library[child_node]
                    else:
                        break
                paths.append(list(reversed(node_path)))
                if len(paths) == len(to_nodes):
                    return paths

            visitedNodes.add(currentNode)

            for nextNode,distanceToNextNode in currentNode.nearNodes.items():

                if nextNode in visitedNodes:
                    continue
                
                if nextNode not in nodeLibrary or nodeLibrary[nextNode] > currentDistance + distanceToNextNode:
                    nodeLibrary[nextNode] = currentDistance + distanceToNextNode
                    parent_library[nextNode] = currentNode

        return paths

if __name__ == '__main__':

    n1 = Node('n1')
    n2 = Node('n2')
    n3 = Node('n3')
    n4 = Node('n4')
    n5 = Node('n5')
    n6 = Node('n6')

    n0 = Node('n0')
    n8 = Node('n8')

    n0.addNearNode(n5,10)
    n8.addNearNode(n2,7)

    n1.addNearNode(n2,9)
    n1.addNearNode(n3,2)
    n1.addNearNode(n5,14)

    n2.addNearNode(n1,9)
    n2.addNearNode(n4,6)
    n2.addNearNode(n8,7)

    n3.addNearNode(n1,2)
    n3.addNearNode(n4,11)
    n3.addNearNode(n5,9)
    n3.addNearNode(n6,10)

    n4.addNearNode(n2,6)
    n4.addNearNode(n3,11)
    n4.addNearNode(n6,15)

    n5.addNearNode(n0,10)
    n5.addNearNode(n1,14)
    n5.addNearNode(n3,9)
    n5.addNearNode(n6,7)

    n6.addNearNode(n3,10)
    n6.addNearNode(n4,15)
    n6.addNearNode(n5,7)

    shortestDistance = n0.distanceTo(n8)

    print(shortestDistance)