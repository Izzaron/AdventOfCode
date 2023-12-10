class Orbiter:
    def __init__(self,_name,_orbits):
        self.name = _name
        self.orbits = _orbits
    
    def __str__(self):
        return self.name
    
    def getNumberOfOrbits(self):
        orbits = self.orbits
        nrOfOrbits = 0
        while(orbits != None):
            orbits = orbits.orbits
            nrOfOrbits += 1
        return nrOfOrbits
    
    def getOrbits(self):
        orbiters = set()
        orbits = self.orbits
        while(orbits != None):
            orbiters.add(orbits)
            orbits = orbits.orbits
        return orbiters

    def orbitalTransfersTo(self,_orbiterTarget):
        orbitersSelf = self.getOrbits()
        orbitersTarget = _orbiterTarget.getOrbits()
        commonOrbiters = orbitersSelf.intersection(orbitersTarget)
        
        return _orbiterTarget.getNumberOfOrbits() + self.getNumberOfOrbits() - 2 * len(commonOrbiters)



def main():
    puzzleInput = open('input6.txt')

    orbiters = dict()

    for line in puzzleInput:
        orbiteeName , orbiterName = line.rstrip().split(')')
        
        if orbiteeName in orbiters:
            orbitee = orbiters[orbiteeName]
        else:
            orbitee = Orbiter(orbiteeName,None)
            orbiters[orbiteeName] = orbitee
        if orbiterName in orbiters:
            orbiter = orbiters[orbiterName]
            orbiter.orbits = orbitee
        else:
            orbiter = Orbiter(orbiterName,orbitee)
            orbiters[orbiterName] = orbiter
    
    #Part 1
    nrOfOrbits = 0
    for _,orbiter in orbiters.items():
        nrOfOrbits += orbiter.getNumberOfOrbits()
    print(nrOfOrbits)

    #Part2
    print(orbiters['YOU'].orbitalTransfersTo(orbiters['SAN']))

if __name__ == '__main__':
    main()