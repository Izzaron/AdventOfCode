import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'test.txt')) as puzzle_input:
    for line in puzzle_input:
        lst = line.split()
        if int(lst[5])!=int(lst[7]):
            print(line)