import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'day1input.txt')
f = open(filename)
numbers = [int(i) for i in f]

for i,num1 in enumerate(numbers):
    for j,num2 in enumerate(numbers[i+1:]):
        for num3 in  numbers[j+1:]:
            if num1+num2+num3==2020:
                print(num1*num2*num3)
                exit()