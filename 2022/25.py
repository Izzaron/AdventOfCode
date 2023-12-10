from math import log
import time

log_2_5 = log(2,5)+1

input_file = __file__.replace('.py','.txt')
test_file = __file__.replace('.py','test.txt')

snafu_dict = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

base5_dict = {
    4: '2',
    3: '1',
    2: '0',
    1: '-',
    0: '='
}

def int2base5(n: int) -> list[int]:
    base5 = []
    i = 1
    while(n>0):
        r = n%(5**i)
        base5.insert(0,int(r))
        n -= r
        i += 1
    return base5

def int_to_base5(n: int,digit_count: int) -> list[int]:
    base5 = []
    r = n
    for i in reversed(range(digit_count)):
        q,r = divmod(r,5**i)
        base5.append(q)
    return base5

def int_to_snafu_digit_count(n: int) -> int:
    return int(log(n,5) + log_2_5)

def int_to_snafu(n: int) -> str:
    digit_count = int_to_snafu_digit_count(n)
    n += (5**digit_count-1)/2
    assert n.is_integer()
    base5 = int2base5(n)
    return ''.join(str(base5_dict[i]) for i in base5)

def snafu_to_int(snafu: str) -> int:
    tot = 0
    for i,s in enumerate(reversed(snafu)):
        tot += snafu_dict[s] * 5**i
    return tot

if __name__ == "__main__":

    start_time = time.time()

    with open(input_file) as puzzle_input:

        snafu_numbers = [line.strip() for line in puzzle_input]
    
    # print(int_to_snafu(sum(snafu_to_int(s) for s in snafu_numbers)))
    n = 15
    c = int_to_snafu_digit_count(n)
    print(int_to_base5(n,c))

    print(time.time() - start_time)