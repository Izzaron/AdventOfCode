f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day16input.txt")

allConstraints = []
section = 1
myticket = []
tickets = []

#read file
for line in f:
    if line == "\n":
        section += 1
        continue
    if "your ticket:" in line:
        continue
    if "nearby tickets:" in line:
        continue
    
    if section == 1:
        key,values = line.split(':')
        allConstraints.append(
            (
                key.strip()
                ,
                [tuple(int(t) for t in c.split('-')) for c in values.split("or")]
            )
        )
    elif section == 2:
        myticket = [int(c) for c in line.split(',')]
    elif section == 3:
        tickets.append([int(c) for c in line.split(',')])

# Part 1
fawltyValues = []
fawltyTickets = []

for i,ticket in enumerate(tickets):
    for value in ticket:
        constraintFails = []
        for constraintPair in [v for k,v in allConstraints]:
            for constraint in constraintPair:
                test = value < constraint[0] or value > constraint[1]
                constraintFails.append(test)
        if all(constraintFails):
            fawltyValues.append(value)
            fawltyTickets.append(i)

# print(sum(fawltyValues))

# Part 2

def conformsToConstraints(value,constraintPair):
    return (value >= constraintPair[0][0] and value <= constraintPair[0][1]) or (value >= constraintPair[1][0] and value <= constraintPair[1][1])

validTickets = [t for i,t in enumerate(tickets) if i not in fawltyTickets]
validTickets.append(myticket)

validTicketsPerField = [[] for i in range(len(myticket))]

for fieldIndex in range(len(myticket)):
    for ticket in validTickets:
        value = ticket[fieldIndex]
        for constraintIndex,constraintPair in enumerate([v for k,v in allConstraints]):
            
            if conformsToConstraints(value,constraintPair):
                validTicketsPerField[fieldIndex].append(constraintIndex)

fieldOrder = [-1 for i in range(len(myticket))]

conformedConstraintsPerField = [len(field) for field in validTicketsPerField]

fieldsToIdentify = [i for i in range(len(myticket))]

while len(fieldsToIdentify) > 0:
    shortestField = min(conformedConstraintsPerField)
    matchingFields = [i for i,f in enumerate(validTicketsPerField) if len(f) == shortestField]
    if len(matchingFields) != 1:
        print("Found multiple hits for ",shortestField)
        exit()
    shortestFieldIndex = matchingFields[0]

    for field in fieldsToIdentify:
        if validTicketsPerField[shortestFieldIndex].count(field) == len(validTickets):
            fieldOrder[shortestFieldIndex] = field
            fieldsToIdentify.remove(field)
            break
    
    conformedConstraintsPerField.remove(shortestField)

print(fieldOrder)

product = 1

for i,fi in enumerate(fieldOrder):
    fieldName = [k for k,v in allConstraints][fi]
    fieldValue = myticket[i]
    print(fieldName,fieldValue)
    if 'departure' in fieldName:
        product *= fieldValue

print(product)

# 2531154960683 too high
# 2325343130651 correct
# 1725637563577 too low