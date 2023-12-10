import re

f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day18input.txt")

def evaluate(expression):
    if len(expression) < 3:
        print("Too short expression: ",expression)
        exit()
    if len(expression)%2 != 1:
        print("Uneven expression: ",expression)
        exit()
    
    if len(expression[0]) != 1:
        toEvaluate = [evaluate(expression[0])]
    else:
        toEvaluate = [expression[0]]

    for i in range(int(len(expression)/2)):
        term1 = expression[(i+1)*2-1]
        if len(term1) != 1:
            term1 = evaluate(term1)
        toEvaluate.append(term1)

        term2 = expression[(i+1)*2]
        if len(term2) != 1:
            term2 = evaluate(term2)
        toEvaluate.append(term2)
        a = eval(''.join(toEvaluate))
        toEvaluate = [str(a)]
    return toEvaluate[0]

def evaluate2(expression):

    if len(expression) < 3:
        print("Too short expression: ",expression)
        exit()
    if len(expression)%2 != 1:
        print("Uneven expression: ",expression)
        exit()

    for i,term in enumerate(expression):
        if len(term) != 1:
            expression[i] = evaluate2(term)

    while '+' in expression:
        plusIndex = expression.index('+')
        expression[plusIndex-1] = str(eval(''.join(expression[plusIndex-1:plusIndex+2])))
        del expression[plusIndex:plusIndex+2]

    # return str(eval(''.join(partial)))
    return str(eval(''.join(expression)))
    

tot = 0

for line in f:
    line = line.strip()
    
    stringLine = '[' + line.replace('(','[').replace(')',']').replace(' ',',').replace('+','\'+\'').replace('*','\'*\'').replace('1','\'1\'').replace('2','\'2\'').replace('3','\'3\'').replace('4','\'4\'').replace('5','\'5\'').replace('6','\'6\'').replace('7','\'7\'').replace('8','\'8\'').replace('9','\'9\'') + ']'

    listedStringLine = eval(stringLine)
    
    partial = int(evaluate2(listedStringLine))

    # print(partial)

    tot += partial

print(tot)