import math
from intcodeprogram import IntcodeProgram
from coordinates import Coordinate, Direction
from collections import defaultdict
from eight import render
from operator import itemgetter,attrgetter

def main():
    puzzleInput = open("input11.txt")
    emergencyHullPaintingRobotSoftware = [int(i) for i in puzzleInput.read().split(',')]
    
    robotBrain = IntcodeProgram(emergencyHullPaintingRobotSoftware,feedbackLoopMode=True)

    currentCoordinate = Coordinate(0,0)
    
    hull = defaultdict(int)

    hull[currentCoordinate.asTuple()] = 1

    paintedCoordinates = set()

    direction = Direction(180)

    while(True):
        colorToPaint, nextDirection = robotBrain.run(hull[currentCoordinate.asTuple()])

        if colorToPaint != 0 and colorToPaint != 1:
            print("Unknown color to paint: ",colorToPaint)
            raise SystemExit

        if hull[currentCoordinate.asTuple()] != colorToPaint:
            paintedCoordinates.add(currentCoordinate.asTuple())

        # Paint
        hull[currentCoordinate.asTuple()] = colorToPaint

        # Turn
        if nextDirection == 0:
            direction += 90
        elif nextDirection == 1:
            direction -= 90
        else:
            print("Unknown next direction: ",nextDirection)
            raise SystemExit

        # Move
        currentCoordinate.stepInDirection(1,direction)

        # Clean up
        if robotBrain.isTerminated:
            break
    
    print(len(paintedCoordinates))
    
    minX = min(hull, key=itemgetter(0))[0]
    maxX = max(hull, key=itemgetter(0))[0]
    minY = min(hull, key=itemgetter(1))[1]
    maxY = max(hull, key=itemgetter(1))[1]
    print(minX,maxX,minY,maxY)
    
    width = abs(maxX - minX)+1
    height = abs(maxY - minY)+1
    print('Width: {}, Height: {}.'.format(width,height))

    # sifImage = [[ str(hull[(x,y)]) if (x,y) in paintedCoordinates else '0' for x in range(minX,maxX)] for y in range(minY,maxY+1)]
    # sifImage = [[ str(hull[(x,y)]) for x in range(minX,maxX+1)] for y in range(minY,maxY+1)]
    sifImage = [str(hull[(x,y)]) for x in range(minX,maxX+1) for y in range(minY,maxY+1)]

    print(len(sifImage))

    render(sifImage,height,width)

if __name__ == '__main__':
    main()