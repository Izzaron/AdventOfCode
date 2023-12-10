from multiprocessing import Pool
import numpy as np
from copy import copy

input_file = __file__.replace('.py','.txt').replace('_2','')
test_file = __file__.replace('.py','test.txt').replace('_2','')

class Buildoption:
    pass

def buildoptions(desired_minerals: list[int], minerals: list[int], miners: list[int] ,time_left: int, blueprint: list[list[int]]) -> Buildoption:
    if time_left == 0: return Buildoption()
    if all([d<=m for d,m in zip(desired_minerals,minerals)]): return Buildoption()
    needed_minerals = [d-m for m,d in zip(minerals,desired_minerals)]
    
    for i in reversed(range(4)):
        if needed_minerals[i] > 0 and miners[i] < 1:
            #buy miner of i
            #return all options => 

    # return option with shortest time

if __name__ == "__main__":

    blueprints: list[list[list[int]]] = []

    with open(test_file) as puzzle_input:

        for line in puzzle_input:
            ln = line.split()
            blueprints.append([
                [int(ln[6]),0,0,0],
                [int(ln[12]),0,0,0],
                [int(ln[18]),int(ln[21]),0,0],
                [int(ln[27]),0,int(ln[30]),0]
            ])
    
    # print(blueprints[0])
    # print(buildoptions([0,0,0,1],[0,0,0,0],[1,0,0,0],24,blueprints[0]))
    bp = np.array(blueprints[0])
    d = np.array([0,0,0,1])
    print(bp)
    c = np.matmul(d,bp)
    print(max(c))