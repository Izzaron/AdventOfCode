from pathfinding import Node
from copy import copy
from itertools import permutations
import time
input_file = __file__.replace('.py','.txt')
test_file = __file__.replace('.py','test.txt')

class Valve(Node):
    def __init__(self, name: str, flow: int) -> None:
        super().__init__(name)
        self.flow       :int            = flow
    
    def __str__(self) -> str:
        return '{}({})->{}'.format(self.name,self.flow,self.nearNodes)
    
    def __repr__(self) -> str:
        return self.name

    def value_at(self, remaining_time: int):
        # print(self.flow,'*',remaining_time,'=',self.flow*remaining_time)
        return self.flow * remaining_time

    def relief(self, remaining_time: int, in_order: list['Valve']):

        in_order = copy(in_order)

        tot_relief = 0

        current_valve = self
        for valve in in_order:
            shortestDistance = current_valve.getShortestDistanceTo(valve)
            if shortestDistance >= remaining_time:
                return tot_relief
            remaining_time -= shortestDistance + 1
            tot_relief += valve.value_at(remaining_time)
            current_valve = valve
        
        return tot_relief

    def self_best_relief(self,remaining_time: int, remaining_valves: list['Valve']):
        max_relief = 0
        for valve in remaining_valves:
            shortestDistance = self.getShortestDistanceTo(valve)
            if shortestDistance >= remaining_time:
                continue
            valve_remaining_time = remaining_time - shortestDistance - 1
            valve_remaining_valves = copy(remaining_valves)
            valve_remaining_valves.remove(valve)
            candidate_relief = valve.value_at(valve_remaining_time) + valve.self_best_relief(valve_remaining_time,valve_remaining_valves)
            max_relief = max(max_relief,candidate_relief)

        return max_relief
    
    @staticmethod
    def best_relief(remaining_time: int, remaining_valves: list['Valve'], current_valve: list['Valve'], cache, operator_count: int = 1):

        if isinstance(remaining_time,int):
            remaining_time = [remaining_time] * operator_count
        
        if isinstance(current_valve,Valve):
            current_valve = [current_valve] * operator_count

        cache_key = tuple(sorted([t for t in zip(current_valve,remaining_time)],key=lambda x: x[0].name) + [v.name for v in remaining_valves])

        if cache_key in cache:
            return cache[cache_key]

        max_relief = 0
        for valve_combination in permutations(remaining_valves,operator_count):
            valve_remaining_valves = copy(remaining_valves)
            operator_relief = [0] * operator_count
            valve_remaining_time = copy(remaining_time)
            valve_current_valve = copy(current_valve)

            for operator_idx in range(operator_count):
                
                operator_valve = valve_combination[operator_idx]
                shortestDistance = valve_current_valve[operator_idx].getShortestDistanceTo(operator_valve)
                
                if shortestDistance >= valve_remaining_time[operator_idx]:
                    continue
                
                valve_remaining_time[operator_idx] -= shortestDistance + 1
                valve_remaining_valves.remove(operator_valve)
                valve_current_valve[operator_idx] = operator_valve
                operator_relief[operator_idx] = operator_valve.value_at(valve_remaining_time[operator_idx])
            
            if len(valve_remaining_valves) == len(remaining_valves):
                continue
            
            next_round_of_relief = Valve.best_relief(valve_remaining_time,valve_remaining_valves,valve_current_valve,cache,operator_count)
            max_relief = max(max_relief,sum(operator_relief)+next_round_of_relief)

        cache[cache_key] = max_relief
        return max_relief
            
if __name__ == "__main__":

    with open(input_file) as puzzle_input:
        lines = puzzle_input.readlines()
    
    # declare valves
    valves: dict[str,Valve] = dict()
    for line in lines:
        line = line.split()
        name = line[1]
        flow = int(line[4].replace('rate=','').replace(';',''))
        valves[name] = Valve(name,flow)
        
    # connect valves
    for line in lines:
        line = line.strip().split('valve')
        name = line[0].split()[1]
        adjecent_names = [adj.strip() for adj in line[1].replace('s ','').split(',')]
        for adj_name in adjecent_names:
            valves[name].addNearNode(valves[adj_name])
    
    time_left = 26
    operator_count = 2
    start_valve = valves['AA']
    useful_valves = sorted([valve for valve in valves.values() if valve.flow > 0],key= lambda x: x.name)
    print(useful_valves)
    start_time = time.time()
    pressure = Valve.best_relief(time_left,useful_valves,start_valve,dict(),operator_count)
    end_time = time.time()
    print(end_time-start_time,pressure)
    # with open(__file__.replace('16.py','result.txt'),'w') as result_file:
    #     result_file.write('{} {} {}'.format(end_time-start_time,pressure,sum(pressure)))
    # start_time = time.time()
    # pressure = start_valve.self_best_relief(time_left,useful_valves)
    # end_time = time.time()
    # print(end_time-start_time,pressure)
    # 2698 too low
    # 2712 too low