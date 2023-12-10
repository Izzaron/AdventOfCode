input_file = __file__.replace('.py','.txt')
test_file = __file__.replace('.py','test.txt')

if __name__ == "__main__":

    with open(test_file) as puzzle_input:

        for line in puzzle_input:
            print(line)