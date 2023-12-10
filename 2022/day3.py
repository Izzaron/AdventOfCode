import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def get_score(c):
    char_num = ord(c)
    if char_num > 96:
        return char_num - 96
    return char_num - 64 + 26

if __name__ == "__main__":

    total_score = 0

    with open(os.path.join(__location__, 'day3input.txt')) as puzzle_input:
        group = []
        for i,line in enumerate(puzzle_input):
            #part 1
            # midpoint = int(len(line)/2)
            # first_half = set(line[:midpoint].strip())
            # second_half = set(line[midpoint:].strip())
            # inter = first_half.intersection(second_half)
            # score = get_score(list(inter)[0])
            # total_score += score

            #part 2
            if (i+1) % 3 == 0:
                group.append(set(line.strip()))

                badge = group[0].intersection(group[1]).intersection(group[2])
                
                score = get_score(list(badge)[0])
                total_score += score

                group = []
            else:
                group.append(set(line.strip()))

    print(total_score)