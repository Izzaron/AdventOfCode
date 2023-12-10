import itertools

f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/day9input.txt")

numbers = [int(line) for line in f]

#part 1
for i,n in enumerate(numbers[25:]):
    combos = itertools.combinations(numbers[i:i+25],2)
    if not any([a+b == n for a,b in combos]):
        print(n)
        break

#part 2
for i,n in enumerate(numbers):
    for j,m in enumerate(numbers[i:]):
        numsum = sum(numbers[i:i+j])
        if numsum == 400480901:
            print(min(numbers[i:i+j])+max(numbers[i:i+j]))
            exit()