f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day5input.txt")

lm = {
    'F': 0,
    'B': 1,
    'R': 1,
    'L': 0,
}

def getSeatID(BSP):
    row = sum([lm[a]*b for a,b in zip(list(BSP[:7]),[64,32,16,8,4,2,1])])
    col = sum([lm[a]*b for a,b in zip(list(BSP[7:]),[4,2,1])])
    return row*8 + col

#Part 1
# print(max([getSeatID(line) for line in f]))

#Part 2
plane = [[0 for col in range(8)] for row in range(128)]

def getSeatRC(BSP):
    row = sum([lm[a]*b for a,b in zip(list(BSP[:7]),[64,32,16,8,4,2,1])])
    col = sum([lm[a]*b for a,b in zip(list(BSP[7:]),[4,2,1])])
    return row, col

for line in f:
    row,col = getSeatRC(line)
    plane[row][col] = 1

for x,row in enumerate(plane):
    for y,col in enumerate(row):
        if col == 0:
            print(x,y)
            print(x*8+y)