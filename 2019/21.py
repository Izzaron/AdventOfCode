from intcodeprogram import IntcodeProgram

input_file = __file__.replace('.py','.txt')
test_file = __file__.replace('.py','test.txt')

class Springdroid:
    def __init__(self,source_code) -> None:
        self.cpu = IntcodeProgram(source_code,feedbackLoopMode=True)
    
    def start(self,instructions: list[str]) -> None:
        self.cpu.run()
        for instruction in instructions:
            response = self.cpu.run(*self.parse_instruction(instruction))
        self.print_response(response)

    def print_response(self,response: list[int]) -> None:
        for c in response:
            try:
                print(chr(c),end='')
            except ValueError:
                print(c)
    
    def parse_instruction(self,command: str) -> list[int]:
        return [ord(c) for c in command]

if __name__ == "__main__":

    with open(input_file) as puzzle_input:
        source_code = [int(i) for i in puzzle_input.read().split(',')]

    # Part 1
    # instructions = [
    #         'NOT C J\n',
    #         'AND D J\n',
    #         'NOT A T\n',
    #         'OR T J\n',
    #         'WALK\n'
    #         ]
        
    # Part 2
    # instructions = [
    #         #!C and D and !E and H
    #         'NOT C J\n',
    #         'AND D J\n',
    #         'NOT E T\n',
    #         'AND T J\n',
    #         # 'NOT H T\n',
    #         'AND H J\n',
            
    #         #!B and (!E or !I) and D
    #         'NOT E T\n',
    #         'NOT T T\n',
    #         'AND I T\n',
    #         'OR B T\n',
    #         'NOT T T\n',
    #         'AND D T\n',
    #         'OR T J\n',

    #         'NOT A T\n',
    #         'OR T J\n',

    #         'RUN\n'
    #         ]

    instructions = [
            
            # !A
            'NOT A J\n',

            # or (!B or !C) and (!F and !I)
            'OR F T\n',
            'OR I T\n',
            'NOT T T\n',
            'AND C T\n',
            'AND B T\n',
            'NOT T T\n',
            'OR T J\n',

            # or !B and !E
            'NOT B T\n',
            'NOT T T\n',
            'OR E T\n',
            'NOT T T\n',
            'OR T J\n',

            # and D
            'AND D J\n',

            'RUN\n'
            ]

    droid = Springdroid(source_code)
    droid.start(instructions)