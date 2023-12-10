import math
import copy
from collections import defaultdict
from operator import itemgetter

def getVisibleAsteroidAngles(xViewer,yViewer,asteroidMap):
    hitAngles = set()
    asteroids = defaultdict(list)
    for y,row in enumerate(asteroidMap):
        for x,pixel in enumerate(row):
            if pixel == '.':
                continue
            if y == yViewer and x == xViewer:
                continue
            dY = (y-yViewer)
            dX = (x-xViewer)
            angle = math.atan2(dY,dX) + 2.5 * math.pi
            if angle >= 2 * math.pi:
                angle -= 2 * math.pi
            hitAngles.add(angle)
            asteroids[angle].append((dX,dY))
    return hitAngles,asteroids

def getClosestAsteroid(asteroidsAtAngle):
    distances = [math.hypot(*i) for i in asteroidsAtAngle]
    indexOfShortestDistance = min(enumerate(distances), key=itemgetter(1))[0]
    return asteroidsAtAngle[indexOfShortestDistance]

def get200TerminadedAsteroid(xViewer,yViewer,_asteroidMap):
    asteroidMap = copy.copy(_asteroidMap)
    nrOfTerminatedAsteroids = 0
    while(True):
        hitAngles,asteroids = getVisibleAsteroidAngles(xViewer,yViewer,asteroidMap)
        if len(hitAngles) == 0:
            return None
        sortedHitAngles = sorted(hitAngles)
        for angle in sortedHitAngles:
            asteroidsAtAngle = asteroids[angle]
            closestAsteroidCoordinates = getClosestAsteroid(asteroidsAtAngle)
            if nrOfTerminatedAsteroids == 199:
                return closestAsteroidCoordinates
            asteroidMap[closestAsteroidCoordinates[1]][closestAsteroidCoordinates[0]] = '.'
            nrOfTerminatedAsteroids += 1

def main():
    asteroidInput = open('input10.txt')

    asteroidMap = [list(row.rstrip()) for row in asteroidInput]

    stationProspect = dict()

    for y,row in enumerate(asteroidMap):
        for x,pixel in enumerate(row):
            if pixel == '#':
                hitAngles,_ = getVisibleAsteroidAngles(x,y,asteroidMap)
                stationProspect[(x,y)] = len(hitAngles)

    bestCandidateCoordinates = max(stationProspect,key=stationProspect.get)
    print(bestCandidateCoordinates,stationProspect[bestCandidateCoordinates])
    relativeCoordsOf200 = get200TerminadedAsteroid(bestCandidateCoordinates[0],bestCandidateCoordinates[1],asteroidMap)
    print((bestCandidateCoordinates[0]+relativeCoordsOf200[0])*100 + bestCandidateCoordinates[1]+relativeCoordsOf200[1])
    # hitAngles,asteroids = getVisibleAsteroidAngles(*bestCandidateCoordinates,asteroidMap)
    # hitAngles
    # sortedHitAngles = sorted(hitAngles)
    # for i,ang in enumerate(hitAngles):
    #     print(ang,sortedHitAngles[i])


if __name__ == '__main__':
    main()