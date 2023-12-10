import os
import copy

directions = {
    'e' : (2,0),
    'se' : (1,-1),
    'sw' : (-1,-1),
    'w' : (-2,0),
    'nw' : (-1,1),
    'ne' : (1,1),
}

def count(tiles):
    blacks = 0
    whites = 0
    for state in tiles.values():
        if state%2 == 0:
            whites += 1
        else:
            blacks += 1

    return blacks

def getNrAdjecent(x,y,tiles):
    adjecent = 0
    for dx,dy in directions.values():
        tilePos = (x+dx,y+dy)
        if tilePos in tiles and tiles[tilePos]%2 != 0:
            adjecent += 1
    return adjecent

def morph(tiles):

    expandedFloor = copy.copy(tiles)

    for tilePos,val in tiles.items():
        for dx,dy in directions.values():
            expandedTilePos = (tilePos[0]+dx,tilePos[1]+dy)
            if expandedTilePos not in expandedFloor:
                expandedFloor[expandedTilePos] = 0

    # visualize(expandedFloor)

    newFloor = copy.copy(expandedFloor)

    for tilePos,val in expandedFloor.items():
        nrAdj = getNrAdjecent(*tilePos,expandedFloor)
        if val%2 == 0: #white
            if nrAdj == 2:
                newFloor[tilePos] +=1
        else: #black
            if nrAdj == 0 or nrAdj > 2:
                newFloor[tilePos] +=1
    
    return newFloor

def visualize(tiles):
    aTile = next(iter(tiles))
    minX = aTile[0]
    maxX = aTile[0]
    minY = aTile[1]
    maxY = aTile[1]
    for x,y in tiles.keys():
        if x < minX:
            minX = x
        if x > maxX:
            maxX = x
        if y < minY:
            minY = y
        if y > maxY:
            maxY = y

    for y in range(maxY,minY-1,-1):
        for x in range(minX,maxX+1):
            if (x,y) in  tiles:
                if tiles[(x,y)]%2 == 0:
                    print('□',end='')
                else:
                    print('■',end='')
            else:
                print(' ',end='')
        print('')


if __name__ == '__main__':

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'day' + str(24) + 'input.txt' )
    f = open(filename)

    tiles = dict()
    
    for line in f:
        line = line.strip()
        index = 0
        x = 0
        y = 0
        while index < len(line):
            if line[index] == 'n' or line[index] == 's':
                dx,dy = directions[line[index:index+2]]
                index += 1
            else:
                dx,dy = directions[line[index]]
            x += dx
            y += dy
            index += 1
        tilePos = (x,y)
        if tilePos in tiles:
            tiles[tilePos] += 1
        else:
            tiles[tilePos] = 1

    # print(0,end=' ')
    # visualize(tiles)
    # count(tiles)
    for i in range(100):
        # print(i+1,end=' ')
        tiles = morph(tiles)
        # visualize(tiles)
        # print(count(tiles))
    print(i+1,count(tiles))