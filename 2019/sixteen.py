# import time

# def basePattern(element,length):
#     base = [0, 1, 0, -1]
#     pattern = [base[0]]*element + [base[1]]*element + [base[2]]*element + [base[3]]*element
#     return [pattern[i%len(pattern)] for i in range(element,length + 1)]

# def flawedFrequencyTransmission(inputSignal):
#     return [int(str(sum([x * y for x, y in zip(inputSignal[i:],basePattern(i+1,len(inputSignal)))]))[-1]) for i in range(len(inputSignal))]

# def main():

#     start_time = time.time()

#     # puzzleInput = open("input16.txt").read()
#     puzzleInput = '03036732577212944063491565474664'

#     print(len(puzzleInput))
#     print("file read --- %s seconds ---" % (time.time() - start_time))

#     inputSignal = [int(s) for s in puzzleInput] * 10000

#     print(len(inputSignal))
#     print("input signal created --- %s seconds ---" % (time.time() - start_time))

#     offset = int(puzzleInput[0:7])

#     for i in range(1,101):
#         inputSignal = flawedFrequencyTransmission(inputSignal)
#         print(i)

#     print(''.join([str(i) for i in inputSignal[offset:offset+8]]))

#     print("done --- %s seconds ---" % (time.time() - start_time))

# if __name__ == '__main__':
#     main()

# part 2 only, cleaned up little bit to make it little more readable

# this is my own library for downloading the input file
input_string = puzzleInput = open("B:/Dropbox/Projects/AdventOfCode/2019/input16.txt").read()
offset = int(input_string[:7], 10)
input_list = list(map(int, input_string)) * 10000
input_length = len(input_list)

for i in range(100):
    partial_sum = sum(input_list[j] for j in range(offset, input_length))
    for j in range(offset, input_length):
        t = partial_sum
        partial_sum -= input_list[j]
        if t >= 0:
            input_list[j] = t % 10
        else:
            input_list[j] = (-t) % 10

            
print(input_list[offset: offset+8])