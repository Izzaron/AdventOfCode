def getPath(currentPosition,instruction,checkIntersections = False, intersection = None, steps = 0):
    distance = int(instruction[1:])
    if instruction[0] == 'R':
        target = (currentPosition[0]+distance,currentPosition[1])
    elif instruction[0] == 'U':
        target = (currentPosition[0],currentPosition[1]+distance)
    elif instruction[0] == 'L':
        target = (currentPosition[0]-distance,currentPosition[1])
    elif instruction[0] == 'D':
        target = (currentPosition[0],currentPosition[1]-distance)
    else:
        print('Instruction neither R, U, L or D')
        exit()
    
    nextStep = currentPosition
    path = []

    while(nextStep != target):
        if instruction[0] == 'R':
            nextStep = (nextStep[0]+1,nextStep[1])
        if instruction[0] == 'U':
            nextStep = (nextStep[0],nextStep[1]+1)
        if instruction[0] == 'L':
            nextStep = (nextStep[0]-1,nextStep[1])
        if instruction[0] == 'D':
            nextStep = (nextStep[0],nextStep[1]-1)
        
        if checkIntersections:
            steps += 1
            if nextStep == intersection:
                return steps
        
        path.append( nextStep )
    
    if checkIntersections:
        return (path,steps)
    else:
        return path
    
def getDistance(position):
    return abs(position[0]) + abs(position[1])

def main():
    input = open("input3.txt")
    wires = []
    for line in input:
        wires.append(line.split(','))

    wire0 = [(0,0)]
    wire1 = [(0,0)]
    
    for instruction0 in wires[0]:
        wire0 += getPath(wire0[-1],instruction0)
    
    for instruction1 in wires[1]:
        wire1 += getPath(wire1[-1],instruction1)
    
    shortestDistance = 1000000000

    wire0path = set(wire0[1:])
    wire1path = set(wire1[1:])

    intersections = wire0path.intersection(wire1path)

    for intersection in intersections:
        distance = getDistance(intersection)
        if distance < shortestDistance:
            shortestDistance = distance
    
    print(shortestDistance)

    #part 2
    interStepDict = dict()
    for intersection in intersections:
        wire0 = [(0,0)]
        wire1 = [(0,0)]
        
        steps = 0
        for instruction0 in wires[0]:
            returnVal = getPath(wire0[-1],instruction0,True,intersection,steps)
            if isinstance(returnVal,int):
                interStepDict[intersection] = returnVal
                break
            (path,steps) = returnVal
            wire0 += path
        
        steps = 0
        for instruction1 in wires[1]:
            returnVal = getPath(wire1[-1],instruction1,True,intersection,steps)
            if isinstance(returnVal,int):
                interStepDict[intersection] += returnVal
                break
            (path,steps) = returnVal
            wire1 += path

    print(min([v for k,v in interStepDict.items()]))


if __name__ == '__main__':
    main()