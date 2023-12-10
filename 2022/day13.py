import os
from functools import cmp_to_key
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

pairs = []

def right_order(a,b):
    if isinstance(a,int):
        if isinstance(b,int):
            if a==b:
                return 0
            else:
                return 1 if a < b else -1
        elif isinstance(b,list):
            return right_order([a],b)
        else:
            raise ValueError()
    elif isinstance(a,list):
        if isinstance(b,int):
            return right_order(a,[b])
        elif isinstance(b,list):
            for i in range(max(len(a),len(b))):
                if i == len(a):
                    return 1
                if i == len(b):
                    return -1
                order = right_order(a[i],b[i])
                if order != 0:
                    return order
            return 0
        else:
            return ValueError()
    else:
        raise ValueError()

if __name__ == "__main__":

    with open(os.path.join(__location__, 'input13.txt')) as puzzle_input:

        pair = ()

        for line in puzzle_input:
            if line == '\n':
                pairs.append(pair)
                pair = ()
            else:
                pair = (*pair,eval(line.strip()))
        pairs.append(pair)
    
    # part 1
    print(sum([i+1 for i,pair in enumerate(pairs) if right_order(pair[0],pair[1]) == 1]))

    # part 2
    lists = [lst for pair in pairs for lst in pair]
    lists.append([[2]])
    lists.append([[6]])

    lists.sort(key=cmp_to_key(right_order))
    lists.reverse()

    print((lists.index([[2]])+1) * (lists.index([[6]])+1))
