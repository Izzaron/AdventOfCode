import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# piece_score = {
#     'X' : 1,
#     'Y' : 2,
#     'Z' : 3
# }

# part 1
# match_score = {
#     'A X' : 3 + 1,
#     'A Y' : 6 + 2,
#     'A Z' : 0 + 3,
#     'B X' : 0 + 1,
#     'B Y' : 3 + 2,
#     'B Z' : 6 + 3,
#     'C X' : 6 + 1,
#     'C Y' : 0 + 2,
#     'C Z' : 3 + 3,
# }

# part 2
match_score = {
    'A X' : 0 + 3,
    'A Y' : 3 + 1,
    'A Z' : 6 + 2,
    'B X' : 0 + 1,
    'B Y' : 3 + 2,
    'B Z' : 6 + 3,
    'C X' : 0 + 2,
    'C Y' : 3 + 3,
    'C Z' : 6 + 1,
}

if __name__ == "__main__":

    total_score = 0

    with open(os.path.join(__location__, 'day2input.txt')) as puzzle_input:
        for line in puzzle_input:
            total_score += match_score[line.strip()]

    print(total_score)