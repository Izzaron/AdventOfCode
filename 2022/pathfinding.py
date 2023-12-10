class Node:
    def __init__(self,name: str):
        self.nearNodes = dict()
        self.directPaths = dict()
        self.name = name
    
    def __str__(self):
        return 'Node<{}>: {}'.format(self.name,self.nearNodes)
    
    def __repr__(self):
        return 'Node<{}>'.format(self.name)

    def addNearNode(self,nearNode: 'Node',distance: int = 1):
        self.nearNodes[nearNode] = distance

    def getShortestDistanceTo(self,endNode: 'Node',excluding: list['Node'] = []):
        startNode = self
        if startNode == endNode:
            return 0
        if endNode in self.directPaths:
            return self.directPaths[endNode]
        nodeLibrary = {startNode: 0}
        visitedNodes = []
        
        while(len(nodeLibrary) > 0):

            currentNode = min(nodeLibrary, key=nodeLibrary.get)

            currentDistance = nodeLibrary[currentNode]
            if currentNode == endNode:
                self.directPaths[endNode] = currentDistance
                return currentDistance
            del nodeLibrary[currentNode]
            visitedNodes.append(currentNode)

            for nextNode,distanceToNextNode in currentNode.nearNodes.items():

                if nextNode in visitedNodes:
                    continue
                    
                if nextNode in excluding:
                    continue
                
                if nextNode not in nodeLibrary or nodeLibrary[nextNode] > currentDistance + distanceToNextNode:
                    nodeLibrary[nextNode] = currentDistance + distanceToNextNode

        return None

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

    shortestDistance = n0.getShortestDistanceTo(n8)

    print(shortestDistance)