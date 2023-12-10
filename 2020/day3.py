f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day3input.txt")

forestMap = [list(line.strip()) for line in f]

def traverse(right,down,map):
    x = 0
    y = 0
    collissions = 0
    for rowIndex in range(len(map)):
        if y >= len(forestMap):
            break
        if isCollision(x,y,map):
            collissions += 1
        x += right
        y += down
    return collissions

def isCollision(x,y,map):
    return map[y][x%len(map[y])] == '#'

first = traverse(1,1,forestMap)
second = traverse(3,1,forestMap)
third = traverse(5,1,forestMap)
fourth = traverse(7,1,forestMap)
fifth = traverse(1,2,forestMap)

print(first)
print(second)
print(third)
print(fourth)
print(fifth)
print(first*second*third*fourth*fifth)