import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

if __name__ == "__main__":

    total_score = 0

    with open(os.path.join(__location__, 'input4.txt')) as puzzle_input:

        for line in puzzle_input:
            elves = line.strip().split(',')
            elf_0 = elves[0].split('-')
            elf_1 = elves[1].split('-')
            elf_0_sections = set(range(int(elf_0[0]),int(elf_0[1])+1))
            elf_1_sections = set(range(int(elf_1[0]),int(elf_1[1])+1))

            # #part 1
            # if elf_0_sections.issubset(elf_1_sections) or elf_1_sections.issubset(elf_0_sections):
            #     total_score += 1

            #part 2
            if len(elf_0_sections.intersection(elf_1_sections)) > 0:
                total_score += 1
            
    print(total_score)