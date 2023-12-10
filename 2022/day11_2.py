import os
from typing import Callable
from inspect import getsourcelines
from math import prod
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

verbose = False

class Monkey:
    def __init__(self,starting_items: list[int], operation_str: str, divisible: int,if_true: int,if_false: int, monkeys: list['Monkey']) -> None:
        self.monkeys = monkeys
        self.items = starting_items
        self.operation = lambda old,div: eval(operation_str)
        self.divisible = divisible
        self.if_true = if_true
        self.if_false = if_false
        self.throw_to_lambda = lambda x: self.if_true if x%self.divisible==0 else self.if_false
        self.inspect_count = 0
    
    def init_items(self):
        for i in range(len(self.items)):
            self.items[i] = [self.items[i]%monkey.divisible for monkey in self.monkeys]
    
    def throw_to(self,x):
        if verbose:
            print('divisible by',self.divisible)
        to_monkey = self.throw_to_lambda(x)
        if verbose:
            print('to monkey',to_monkey)
        return to_monkey

    def inspect(self,items: list[int]) -> int:
        if verbose:
            print('Worry level: ',item)
        self.inspect_count += 1
        rtn = [self.operation(item,self.monkeys[i].divisible)%self.monkeys[i].divisible for i,item in enumerate(items)]
        if verbose:
            print('Worry level: ',rtn)
        return rtn

    def take_turn(self):
        throws: list[tuple[int,int]] = []
        while(len(self.items) > 0):
            item = self.inspect(self.items.pop(0))
            throws.append((item,self.throw_to(item[self.monkeys.index(self)])))
        if verbose:
            print()
        return throws
    
    def print_functions(self):
        print(str(getsourcelines(self.operation)[0]).strip("['\\n']").split(" = ")[1])
        print(str(getsourcelines(self.throw_to)[0]).strip("['\\n']").split(" = ")[1])

if __name__ == "__main__":

    with open(os.path.join(__location__, 'input11.txt')) as puzzle_input:
        all_lines = [line.strip().split() for line in puzzle_input.readlines()]

    monkeys: list[Monkey] = []

    i = 0
    while(i < len(all_lines)):
        if len(all_lines[i]) == 0:
            i += 1
            continue
        if all_lines[i][0] == 'Monkey':
            i += 1
            items = [int(item.replace(',','')) for item in all_lines[i][2:]]
            i += 1
            op_str = ' '.join(all_lines[i][-3:])
            op_str += "%div"
            i += 1
            divisible = int(all_lines[i][-1])
            i += 1
            if_true = int(all_lines[i][-1])
            i += 1
            if_false = int(all_lines[i][-1])
            monkeys.append(Monkey(items,op_str,divisible,if_true,if_false,monkeys))
        i += 1

    for monkey in monkeys:
        monkey.init_items()
    # for monkey in monkeys:
    #     monkey.print_functions()

    # for monkey in monkeys:
    #     print(monkey.items)

    nr_of_rounds = 10000

    last_inspect_count = [0] * len(monkeys)

    for round in range(1,nr_of_rounds+1):
        if round%100 == 0:
            print(round)
        for i,monkey in enumerate(monkeys):
            if verbose:
                print('Monkey',i)
            throws = monkey.take_turn()
            for item,throw_to in throws:
                monkeys[throw_to].items.append(item)
        inspect_count = [monkey.inspect_count for monkey in monkeys]
        # print(round,inspect_count)
        # print(round,[inspect_count[i] - last_inspect_count[i] for i in range(len(monkeys))],sum(inspect_count[i] - last_inspect_count[i] for i in range(len(monkeys))))
        last_inspect_count = inspect_count

    if verbose:
        for monkey in monkeys:
            print(monkey.inspect_count,monkey.items)
    
    # print(inspect_count)
    print(prod(sorted([monkey.inspect_count for monkey in monkeys])[-2:]))