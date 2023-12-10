input = open("input4.txt").read()

(minPass,maxPass) = [int(i) for i in input.split('-')]

def isValidPassword(password):
    password = str(password)

    occurences = dict.fromkeys(password,0)

    lastC = password[0]

    occurences[lastC] += 1

    concurrency = False

    for c in password[1:]:

        if int(c) < int(lastC):
            return False
        
        if c == lastC:
            concurrency = True
        
        occurences[c] += 1
        
        lastC = c
    
    occurency = False
    for _,v in occurences.items():
        if v == 2:
            occurency = True
    
    return concurrency and occurency

numOfPasses = 0
for p in range(minPass,maxPass+1):
    if isValidPassword(p):
        numOfPasses += 1
        print(p)

print(numOfPasses)