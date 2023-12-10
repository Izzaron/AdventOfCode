import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# #part 1
# def move_crates(amount,from_stack,to_stack):
#     for _ in range(amount):
#         to_stack.append(from_stack.pop())

#part 2
def move_crates(amount,from_stack,to_stack):
    to_stack += from_stack[-amount:]
    if amount > 0:
        del from_stack[-amount:]

if __name__ == "__main__":

    with open(os.path.join(__location__, 'input5.txt')) as data:

        puzzle_input = data.readlines()

    for line in puzzle_input:
        try:
            if line[1] == '1':
                nr_of_stacks = len(line.strip().split())
                break
        except IndexError:
            continue

    stacks = [[] for _ in range(nr_of_stacks)]
    stack_positions = [(1+4*i) for i in range(nr_of_stacks)]

    first_half = True

    for line in puzzle_input:
        if first_half:
            try:
                if line[1] == '1':
                    first_half = False
                    for stack in stacks:
                        stack.reverse()
                    continue
                for i,index in enumerate(stack_positions):
                    crate = line[index]
                    if crate == ' ':
                        continue
                    stacks[i].append(crate)
            except IndexError:
                continue
        else:
            if line != '\n':
                instructions = line.split()
                amount = int(instructions[1])
                from_stack = int(instructions[3]) - 1
                to_stack = int(instructions[5]) - 1
                move_crates(amount,stacks[from_stack],stacks[to_stack])

    ans = [stack[-1] for stack in stacks]
    print(''.join(ans))