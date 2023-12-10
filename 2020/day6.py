f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day6input.txt")

groupAnswers = []
answer = set()
groupAnswers.append(answer)
firstLine = True
for line in f:
    if line == "\n":
        firstLine = True
        continue

    if firstLine:
        answer = set(line.strip())
        groupAnswers.append(answer)
    else:
        answer.intersection_update(set(line.strip())) # without "intersection_" for part 1
    firstLine = False

for line in groupAnswers:
    print(line)

print(sum([len(s) for s in groupAnswers]))