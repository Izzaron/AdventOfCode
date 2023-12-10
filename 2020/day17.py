from copy import copy,deepcopy

class Cube:
    def __init__(self,x,y,z,w,state):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.isActive = state
    
    def coordinates(self):
        return (self.x,self.y,self.z,self.w)

    def getNeighbourhood(self):
        neighbourhood = []
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                for z in [-1,0,1]:
                    for w in [-1,0,1]:
                        neighbourhood.append( (self.x+x,self.y+y,self.z+z,self.w+w) )
        return neighbourhood


class PocketDimension:
    def __init__(self):
        self.cubes = dict()
        self.cycle = 0

    def addCube(self,cube):
        self.cubes[cube.coordinates()] = cube
    
    def hasActiveCubeAt(self,coordinates):
        if coordinates in self.cubes and self.cubes[coordinates].isActive:
            return True
        else:
            return False

    def readInput(self,f):
        y = 0
        for line in f:
            x = 0
            for char in line.strip():
                self.addCube(Cube(x,y,0,0,char=='#'))
                x += 1
            y += 1

    def simulate(self):

        #find neighbourhood of active cubes
        coordinatesToCheck = set()
        
        for cube in self.cubes.values():
            if cube.isActive:
                neighbourhood = cube.getNeighbourhood()
                for coordinate in neighbourhood:
                    coordinatesToCheck.add(coordinate)

        #activate/decativate neighbourhood and active cubes
        nextGeneration = dict()

        for coordinate in coordinatesToCheck:
            self.updateState(coordinate,nextGeneration)

        self.cubes = nextGeneration

        self.cycle += 1

    def updateState(self,coordinate,nextGeneration):

        if self.hasActiveCubeAt(coordinate):
            cube = copy(self.cubes[coordinate])
            aciveCubesInNeighbourhood = [self.hasActiveCubeAt(c) for c in cube.getNeighbourhood()]
            if sum(aciveCubesInNeighbourhood) == 3 or sum(aciveCubesInNeighbourhood) == 4: #includes the cube itself
                nextGeneration[coordinate] = cube

        else:
            if coordinate in self.cubes:
                cube = copy(self.cubes[coordinate])
            else:
                cube = Cube(*coordinate,False)
            aciveCubesInNeighbourhood = [self.hasActiveCubeAt(c) for c in cube.getNeighbourhood()]
            
            if sum(aciveCubesInNeighbourhood) == 3: #not including the cube itself since its not active
                cube.isActive = True
                nextGeneration[coordinate] = cube

    def activeCubes(self):
        return sum([c.isActive for c in self.cubes.values()])


    def visualize(self):
        #only works for 3d

        print('Cycle = ',self.cycle)
        minZ = min(self.cubes.values(),key=lambda c: c.z).z
        minZ = min(minZ,0)
        maxZ = max(self.cubes.values(),key=lambda c: c.z).z
        minY = min(self.cubes.values(),key=lambda c: c.y).y
        minY = min(minY,0)
        maxY = max(self.cubes.values(),key=lambda c: c.y).y
        minX = min(self.cubes.values(),key=lambda c: c.x).x
        minX = min(minX,0)
        maxX = max(self.cubes.values(),key=lambda c: c.x).x

        # print('x(',minX,',',maxX,'), y(',minY,',',maxY,'), z(',minZ,',',maxZ,')')

        for z in range( minZ , maxZ+1 ):
            print('z =',z)
            for y in range( minY , maxY+1 ):
                for x in range( minX , maxX+1 ):
                    if self.hasActiveCubeAt((x,y,z)):
                        print('#',end='')
                    else:
                        print('.',end='')
                print()
            print()


f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day17input.txt")

space = PocketDimension()
space.readInput(f)

for i in range(6):
    space.simulate()

print('cycle: ',space.cycle,' active cubes: ',space.activeCubes())