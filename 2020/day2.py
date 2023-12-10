f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day2input.txt")

validPasswords = 0
validPasswords2 = 0

for line in f:
    protocol,password = line.split(':')
    password = password.strip()
    letter = protocol[-1]
    protocol = protocol[:-1]
    prList = protocol.split('-')
    lowerBound = int(prList[0])
    upperBound = int(prList[1])

    letterOccurrence = list(password).count(letter)

    if letterOccurrence >= lowerBound and letterOccurrence <= upperBound:
        validPasswords += 1

    if (password[lowerBound-1] == letter) ^ (password[upperBound-1] == letter):
        validPasswords2 += 1

print(validPasswords)
print(validPasswords2)