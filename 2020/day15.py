f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day15input.txt")
line = [l for l in f][0]
numbers = [int(c) for c in line.split(',')]

# it = len(numbers)
# stopAt = 2020
# shouldPrint = 1

# while(it<stopAt):
#     if not numbers[-1] in numbers[:-1]:
#         numbers.append(0)
#     else:
        
#         lastIndex = len(numbers) - 2 - numbers[:-1][::-1].index(numbers[-1])
#         numbers.append(len(numbers) - 1 - lastIndex)
    
#     it += 1
#     if it > shouldPrint:
#         print(it,it/stopAt*100)
#         shouldPrint *= 10

# print(numbers[-1])

#part 2

# numbers = [0,3,6]

shouldPrint = 1

lastOccurence = dict()

for i,lastNumber in enumerate(numbers):
    lastOccurence[lastNumber] = i

stopAt = 30000000

while(i<stopAt):

    lastLastNumber = lastNumber

    if lastOccurence[lastNumber] == i:
        lastNumber = 0
        
    else:
        lastNumber = i - lastOccurence[lastNumber]
        if not lastNumber in lastOccurence:
            lastOccurence[lastNumber] = i+1
        lastOccurence[lastLastNumber] = i

    i += 1

    if i > shouldPrint:
        print(i,i/stopAt*100)
        shouldPrint *= 10

print(lastLastNumber)

# 0360331040