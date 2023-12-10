from multiprocessing import Pool
import time
import numpy as np

input_file = __file__.replace('.py','.txt')
test_file = __file__.replace('.py','test.txt')

class Factory:
    def __init__(self) -> None:
        self.buildoptions   : list[list[int]]   = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]]

    def simulate(self,time_left: int, blueprint: list[list[int]],stop_min: list[int]) -> int:
        
        minerals = (0,0,0,0)
        miners   = (1,0,0,0)
        blueprint += [[0,0,0,0]]

        return self.construct_with(minerals,miners,time_left,blueprint,stop_min)[3]

    def construct_with(self, minerals: tuple[int,int,int,int], miners: tuple[int,int,int,int], time_left: int, blueprint: list[list[int]],stop_min: list[int]) -> tuple[int,int,int,int]:

        if time_left == 0:
            return minerals

        options = []

        for i in [t for idx,t in enumerate([0,1,2,3,4]) if time_left > [16,7,4,0,0][idx] and (minerals+(0,))[idx] < stop_min[idx]]:
            if all(mineral>=cost for mineral,cost in zip(minerals,blueprint[i])):
                minerals_to_send    = tuple(bank+produced-cost for bank,produced,cost in zip(minerals,miners,blueprint[i]))
                miners_to_send      = tuple(have+built for have,built in zip(miners,self.buildoptions[i]))
                result = self.construct_with(minerals_to_send,miners_to_send,time_left-1,blueprint,stop_min)
                options.append(result)

        return max(options,key=lambda x: x[3])

if __name__ == "__main__":

    blueprints: list[list[list[int]]] = []

    with open(input_file) as puzzle_input:

        for line in puzzle_input:
            ln = line.split()
            blueprints.append([
                [int(ln[6]),0,0,0],
                [int(ln[12]),0,0,0],
                [int(ln[18]),int(ln[21]),0,0],
                [int(ln[27]),0,int(ln[30]),0]
            ])
    
    time_left = 32

    start_time = time.time()

    # stop_mins = [[6,14,7,100,1],[6,8,12,100,1]] #test
    stop_mins = [[9,15,11,100,1],[9,16,21,100,1],[9,14,18,100,1]]

    blueprints = blueprints[:3]

    with Pool() as p:
        geode = p.starmap(Factory().simulate,zip([time_left]*len(blueprints),blueprints,stop_mins))

    print('time:',time.time()-start_time)
    
    quality = [(i+1)*g for i,g in enumerate(geode)]

    print(geode)
    print(quality)
    print(sum(quality))
    print(np.prod(geode))
 
    with open(__file__.replace('.py','result_2.txt'),'w') as result_file:
        result_file.write('{}\n{}'.format(str(geode),str(np.prod(geode))))
    # part 2 6660 too low