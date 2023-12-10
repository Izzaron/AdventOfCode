import numpy as np
import collections

import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'day20input.txt')
f = open(filename)

class Tile:
    def __init__(self,idNumber,matrix):
        self.idNumber = idNumber
        self.matrix = np.matrix(matrix)
        self.permutation = 0
    
    def visualize(self):
        print(self.idNumber)
        print(self.matrix)

    def flip(self,axis=None):
        #axis = None    flips both axis (transpose)
        #axis = 0       flips up/down
        #axis = 1       flips right/left
        self.matrix = np.flip(self.matrix,axis)
        if type(self.matrix.item(0,0)) is Tile:
            for i in range(self.matrix.shape[0]):
                for j in range(self.matrix.shape[1]):
                    self.matrix.item(i,j).flip(axis)
            
    
    def rot90(self,k=1):
        #rotates 90 degrees counter-clockwise k times
        self.matrix = np.rot90(self.matrix,k)
        if type(self.matrix.item(0,0)) is Tile:
            for i in range(self.matrix.shape[0]):
                for j in range(self.matrix.shape[1]):
                    self.matrix.item(i,j).rot90(k)
    
    def edge(self,k):
        if k == 0: #right
            return tuple(self.matrix.T[-1,:].tolist()[0])
        elif k == 1: #top
            return tuple(self.matrix[0,:].tolist()[0])
        elif k == 2: #left
            return tuple(self.matrix.T[0,:].tolist()[0])
        elif k == 3: #bottom
            return tuple(self.matrix[-1,:].tolist()[0])
    
    def permute(self):

        self.rot90()

        returnStr = "rotated"
        
        if self.permutation == 3:
            self.flip(0)
            returnStr += " and flipped"

        self.permutation = (self.permutation + 1)%4

        return returnStr

    def getInner(self):
        return self.matrix[1:9,1:9]
    
    def combineInner(self):
        for i in range(self.matrix.shape[0]):
            for j in range(self.matrix.shape[1]):
                if j == 0:
                    pictureRow = self.matrix.item(i,j).getInner()
                else:
                    pictureRow = np.concatenate((pictureRow,self.matrix.item(i,j).getInner()),axis=1)
            if i == 0:
                combinedMatrix = pictureRow
            else:
                combinedMatrix = np.concatenate((combinedMatrix,pictureRow),axis=0)
        
        return combinedMatrix
    
    def sum(self):
        return np.sum(self.matrix)

    def innerSum(self):
        return np.sum(self.combineInner())

    def __str__(self):
        return self.matrix.__str__()
    
    def __repr__(self):
        return str(self.idNumber)

class EdgeLibrary:
    def __init__(self):
        self.edges = dict()
        self.redges = dict()
        self.tiles = dict()
    
    def addEdge(self,edge,tile=None):
        if edge in self.edges:
            self.edges[edge] += 1
            if tile:
                self.tiles[edge].append(tile)
        elif edge in self.redges:
            self.edges[self.redges[edge]] += 1
            if tile:
                self.tiles[self.redges[edge]].append(tile)
        else:
            self.edges[edge] = 1
            self.redges[tuple(reversed(edge))] = edge
            self.tiles[edge] = [tile]
    
    def addTile(self,tile):
        for k in range(4):
            self.addEdge(tile.edge(k),tile)
    
    def occurenceOf(self,edge):
        if edge in self.edges:
            return self.edges[edge]
        else:
            if edge in self.redges:
                redge = self.redges[edge]
                return self.edges[redge]
            else:
                return 0
    
    def getConnectedTile(self,tile,edge):
        if edge in self.tiles:
            return next((connectedTile for connectedTile in self.tiles[edge] if connectedTile is not tile),None)
        else:
            if edge in self.redges:
                return next((connectedTile for connectedTile in self.tiles[self.redges[edge]] if connectedTile is not tile),None)
            else:
                return None

def readFile(f):
    tiles = []

    for line in f:
        if 'Tile' in line:
            idNumber = int(line.replace('Tile','').replace(':',''))
            matrix = []
            for _ in range(10):
                line = f.readline().strip()
                matrix.append(
                    [1 if c == '#' else 0 for c in line]
                    )

            tiles.append(Tile(idNumber,matrix))
    
    return tiles

def findPattern(pattern,matrix):
    listPattern = []
    for line in pattern:
        listPattern.append(
            [1 if c == '#' else 0 for c in line]
            )
    matrixPattern = np.matrix(listPattern)

    hits = 0

    mHeight = matrix.shape[0]
    mWidth = matrix.shape[1]
    pHeight = matrixPattern.shape[0]
    pWidth = matrixPattern.shape[1]

    for i in range(mHeight - pHeight+1):
        for j in range(mWidth - pWidth+1):
            if (np.logical_and(matrix[i:(i+pHeight),j:(j+pWidth)],matrixPattern) == matrixPattern).all():
                hits += 1
    
    return hits

tiles = readFile(f)

#save number of occurence of each edge
edges = EdgeLibrary()
for tile in tiles:
    edges.addTile(tile)

#get tiles with exactly two edges with occurence = 1 (the corners)
corners = []
for tile in tiles:
    oneEdges = 0
    for k in range(4):
        edge = tile.edge(k)
        if edges.occurenceOf(edge) == 1:
            oneEdges += 1
    if oneEdges == 2:
        corners.append(tile)

#get the product of the corner id numbers
# prod = 1
# for corner in corners:
#     print(corner.idNumber)
#     prod *= corner.idNumber

# print(prod)

#part 2

#start filling the whole picture at a corner
corner = corners[0]

#rotate the corner so that the number of bordering tiles is 1 upwards and to the left
while not (edges.occurenceOf( corner.edge(1) ) == 1 and edges.occurenceOf( corner.edge(2) ) == 1):
    corner.permute()

#fill in the rest of the tiles
row = [corner]
picture = []

for i in range(12):

    for j in range(1,12):

        previousTile = row[j-1]

        #find the tiles connected to the right
        nextTile = edges.getConnectedTile(previousTile,previousTile.edge(0))

        #rotate/flip the next edge so that its left edge matches the currents right edge
        while previousTile.edge(0) != nextTile.edge(2):
            nextTile.permute()

        #add the new tile to the row
        row.append(nextTile)
    
    #add the new row to the picture
    picture.append(row)

    #if not on the last row:
    if i != 11:
        upperTile = row[0]

        #find the first tile of the next row by checking what fits the down edge of the first tile of this row.
        downTile = edges.getConnectedTile(upperTile,upperTile.edge(3))
    
        #flip/rotate the first tile of the next row until its upper edge matches the first tile of this rows down edge
        while upperTile.edge(3) != downTile.edge(1):
            downTile.permute()

        #start a new row
        row = [downTile]

#convert the new 2d list into a matrix
pictureTile = Tile(0,picture)

#define the pattern to look for
seaMonster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]

#flip/rotate the whole picture until the pattern is found
permutation = 1
while findPattern(seaMonster,pictureTile.combineInner()) == 0:
    print('Permutation ',permutation)
    print(pictureTile.permute())
    permutation += 1
    if permutation > 8:
        break

monsters = findPattern(seaMonster,pictureTile.combineInner())
dots = np.sum(pictureTile.combineInner())

print('monsters',monsters)
print('dots',dots)
print('habitat',dots-monsters*15)