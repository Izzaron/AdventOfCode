import copy

f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/Day11input.txt")

def isOccupied(x,y,seatMap):
    if x < 0 or y < 0:
        return False
    if x >= len(seatMap[0]) or y >= len(seatMap):
        return False
    
    seat = seatMap[y][x]
    if seat == "#":
        return True
    else:
        return False

def isAttractive(x,y,seatMap):
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i == 0 and j == 0:
                continue
            m = 1
            while True:
                if x+m*i < 0 or y+m*j < 0:
                    break
                if x+m*i >= len(seatMap[0]) or y+m*j >= len(seatMap):
                    break
                if seatMap[y+m*j][x+m*i] == ".":
                    m += 1
                else:
                    break
            if isOccupied(x+m*i,y+m*j,seatMap):
                return False
    return True

def isUnattractive(x,y,seatMap):
    nrOccupied = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i == 0 and j == 0:
                continue
            m = 1
            while True:
                if x+m*i < 0 or y+m*j < 0:
                    break
                if x+m*i >= len(seatMap[0]) or y+m*j >= len(seatMap):
                    break
                if seatMap[y+m*j][x+m*i] == ".":
                    m += 1
                else:
                    break
                
            if isOccupied(x+m*i,y+m*j,seatMap):
                nrOccupied += 1
    if nrOccupied > 4:
        return True
    else:
        return False

def nrOccupiedSeats(seatMap):
    return sum([rows.count("#") for rows in seatMap])

def printSection(height,width,seatMap):
    for row in seatMap[:height]:
        print("".join(row[:width]))
    print("")

seatMap = [[c for c in line.strip()] for line in f]

while True:
    # printSection(10,10,seatMap)
    occupiedBefore = nrOccupiedSeats(seatMap)
    newSeatMap = copy.deepcopy(seatMap)
    for y,row in enumerate(seatMap):
        for x,seat in enumerate(row):
            seat = seatMap[y][x]
            if seat == ".":
                continue
            elif seat == "#" and isUnattractive(x,y,seatMap):
                newSeatMap[y][x] = "L"
            elif seat == "L" and isAttractive(x,y,seatMap):
                newSeatMap[y][x] = "#"
            
    occupiedAfter = nrOccupiedSeats(newSeatMap)
    if occupiedBefore == occupiedAfter:
        print(occupiedAfter)
        break
    seatMap = newSeatMap