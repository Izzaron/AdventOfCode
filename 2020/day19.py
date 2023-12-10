from copy import copy

f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day19input.txt")

def parseRule(line,ruleBook):
    nr,rule = line.split(':')
    
    if rule.strip() == '\"a\"':
        ruleBook[nr] = 'a'
        return
    elif rule.strip() == '\"b\"':
        ruleBook[nr] = 'b'
        return

    if '|' in rule:
        parts = rule.split('|')
        ruleBook[nr] = [parts[0].split(),parts[1].split()]
    else:
        ruleBook[nr] = rule.split()

parsingRules = True
ruleBook = dict()
examples = []
messages = []

for line in f:
    # print(line.strip())
    if line == '\n':
        parsingRules = False
        continue

    if parsingRules:
        parseRule(line.strip(),ruleBook)
    else:
        messages.append(line.strip())

# for nr,rule in ruleBook.items():
#     print(nr,rule)

# for nr in ['0','8','11','42','31']:
#     print(nr,ruleBook[nr])

def processRule(rule,ruleBook):

    for i,subRule in enumerate(rule):
        if subRule == 'a' or subRule == 'b':
            pass
        else:
            try:
                rule[i] = ruleBook[subRule]
            except:
                print(rule)
                exit()
    # print(rule)
    newRules = [rule]
    
    done = False
    while not done:
        newNewRules = []
        done = True
        for newRule in newRules:
            nextList = next((sr for sr in newRule if type(sr[0]) is list), None)

            if nextList:
                done = False
                for nl in nextList:
                    # print(nl)
                    newRuleN = copy(newRule)
                    # print(newRuleN)
                    newRuleN[newRule.index(nextList):newRule.index(nextList)+1] = nl
                    # print(newRuleN)
                    newNewRules.append(newRuleN)
                newRules = newNewRules
    
    for nr in newRules:
        for i,sr in enumerate(nr):
            if type(sr) is list:
                nr[i:i+1] = sr
    
    return newRules

done = False
rules = [ruleBook['0']]
while not done:
    # print('before:')
    # for rule in rules:
    #     print(rule)
    newRules = []
    for rule in rules:
        newRules += processRule(rule,ruleBook)
    # print('after:')
    # for rule in newRules:
    #     print(rule)
    print(len(newRules))
    done = True
    for rule in rules:
        if any([sr != 'a' and sr != 'b' for sr in rule]):
            done = False
            rules = newRules
            break

compactedRules = [''.join(rule) for rule in rules]
# for cr in compactedRules:
#     print(cr)

answer = sum([m in compactedRules for m in messages])

print(answer)