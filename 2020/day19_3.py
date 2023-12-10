import time

t0 = time.perf_counter()

f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day19input.txt")

#Parse rules

def parseRule(line,ruleBook):
    if line == "8: 42":
        line = "8: 42 | 42 8"
    if line == "11: 42 31":
        line = "11: 42 31 | 42 11 31"
    nr,rule = line.split(':')
    
    if rule.strip() == '\"a\"':
        ruleBook[int(nr)] = 'a'
        return
    elif rule.strip() == '\"b\"':
        ruleBook[int(nr)] = 'b'
        return

    if '|' in rule:
        parts = rule.split('|')
        ruleBook[int(nr)] = [
            [int(r) for r in parts[0].split()],
            [int(r) for r in parts[1].split()],
            ]
    else:
        ruleBook[int(nr)] = [int(r) for r in rule.split()]
        

parsingRules = True
ruleBook = dict()
messages = []

for line in f:
    if line == '\n':
        parsingRules = False
        continue

    if parsingRules:
        parseRule(line.strip(),ruleBook)
    else:
        messages.append(line.strip())

#Test rules

def testRule(message,pos,rule):
    # printMsg = list(message)
    # printMsg[pos] = '\u001b[36m' + message[pos] + '\u001b[0m'
    # print(''.join(printMsg),rule)

    if type(rule) is str:
        if message[pos] == rule:
            return [pos+1]
        else:
            return [pos]
    elif type(rule[0]) is list:

        alternativePositions = []
        for alternative in rule:
            alternativePositions += testRule(message,pos,alternative)
        return alternativePositions

    else:

        newPositions = testRule(message,pos,ruleBook[rule[0]])

        newPositions = [newPos for newPos in newPositions if newPos > pos]

        if len(rule) > 1:
            
            advancedPositions = []
            for newPos in newPositions:
                if not newPos >= len(message):
                    advancedPositions += testRule(message,newPos,rule[1:])
            newPositions = advancedPositions
            newPositions = [newPos for newPos in newPositions if newPos > pos and not newPos > len(message)]
        
        return newPositions

def validate(message,rule):
    return any(finalPositions == len(message) for finalPositions in testRule(message,0,rule))

print(sum([validate(mes,ruleBook[0]) for mes in messages]))

t1 = time.perf_counter()

print((t1-t0)*1000)