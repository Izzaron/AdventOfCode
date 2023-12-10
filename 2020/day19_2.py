from copy import copy

f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day19input_test2.txt")

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

for nr,rule in sorted(ruleBook.items()):
    print(nr,rule)

# for message in messages:
#     print(message)

def testRule(message,pos,rule):
    printMsg = list(message)
    # printMsg[pos] = '\u001b[36m' + message[pos] + '\u001b[0m'
    printMsg[pos] = message[pos].upper()
    print(''.join(printMsg),rule)

    if type(rule) is str:
        if message[pos] == rule:
            return pos+1
        else:
            return pos
    elif type(rule[0]) is list:
        
        for alternative in rule:
            newPos = testRule(message,pos,alternative)
            if newPos > pos:
                return newPos
        return pos # which is equal to newPos or function would have returned already

    else:
        tryPos = pos
        for i,subRule in enumerate(rule):
            newPos = testRule(message,tryPos,ruleBook[subRule])

            #whole message is consumed before all rules are
            if newPos >= len(message) and i != len(rule) - 1:
                return pos
            #allows to succeed if whole message is consumed, even if all rules arent consumed
            # if newPos >= len(message):
            #     return newPos
            #if one part fails the whole rule fails
            elif newPos == tryPos:
                return pos
            #the pos has advanced and so somewhere the rules have been obeyed
            else:
                tryPos = newPos
        
        return newPos

def validate(message,rule):
    return testRule(message,0,rule) == len(message)

# for mes in messages:
#     rule = ruleBook[0]
#     print(mes,testRule(mes,0,rule) == len(mes))

# print(0,ruleBook[0])
# print(8,ruleBook[8])
# print(11,ruleBook[11])

# mes = 'babbbbaabbbbbabbbbbbaabaaabaaa'    #fails      but should succeed
mes = 'bbabbbbaabaabba'                   #succeeds   and should succeed
# mes = 'babaaabbbaaabaababbaabababaaab'      #fails      and should fail
# mes = 'aaaabbaaaabbaaa'                     #succeeds but should fail

print(validate(mes,ruleBook[0]))

# print(sum([validate(mes,ruleBook[0]) for mes in messages]))
# for m in messages:
#     if validate(m,ruleBook[0]):
#         print(m)

# 246 too low
# 353 too high

# allMessages = [
#     'abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa',
#     'bbabbbbaabaabba',
#     'babbbbaabbbbbabbbbbbaabaaabaaa',
#     'aaabbbbbbaaaabaababaabababbabaaabbababababaaa',
#     'bbbbbbbaaaabbbbaaabbabaaa',
#     'bbbababbbbaaaaaaaabbababaaababaabab',
#     'ababaaaaaabaaab',
#     'ababaaaaabbbaba',
#     'baabbaaaabbaaaababbaababb',
#     'abbbbabbbbaaaababbbbbbaaaababb',
#     'aaaaabbaabaaaaababaa',
#     'aaaabbaaaabbaaa',
#     'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa',
#     'babaaabbbaaabaababbaabababaaab',
#     'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba',
# ]

# correctMessages = [
#     'bbabbbbaabaabba',
#     'babbbbaabbbbbabbbbbbaabaaabaaa',
#     'aaabbbbbbaaaabaababaabababbabaaabbababababaaa',
#     'bbbbbbbaaaabbbbaaabbabaaa',
#     'bbbababbbbaaaaaaaabbababaaababaabab',
#     'ababaaaaaabaaab',
#     'ababaaaaabbbaba',
#     'baabbaaaabbaaaababbaababb',
#     'abbbbabbbbaaaababbbbbbaaaababb',
#     'aaaaabbaabaaaaababaa',
#     'aaaabbaabbaaaaaaabbbabbbaaabbaabaaa',
#     'aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba',
# ]

# for msg in messages:
#     if msg not in correctMessages:
#         print(msg)

# bbabbbbaabaabba
# aaabbbbbbaaaabaababaabababbabaaabbababababaaa
# ababaaaaaabaaab
# ababaaaaabbbaba
# baabbaaaabbaaaababbaababb
# aaaabbaabbaaaaaaabbbabbbaaabbaabaaa