import os
from coordinates import Coordinate
from pathfinding import Node
from holstcollections import ValueSortedDict
from collections import defaultdict
from multiprocessing import Pool
import sys
import cProfile
import time
from enum import Enum
from copy import copy

sys.setrecursionlimit(10000)
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class NodeKind(Enum):
        entrance = 1
        door = 2
        key = 3

class TunnelNode(Node):
    
    def __init__(self, name: str, kind: NodeKind):
        self.kind: NodeKind = kind
        super().__init__(name)

    def am_entrance(self) -> bool:
        return self.kind == NodeKind.entrance

    def am_door(self) -> bool:
        return self.kind == NodeKind.door

    def am_key(self) -> bool:
        return self.kind == NodeKind.key
    
    @staticmethod
    def kind(symbol: str) -> NodeKind:
        if symbol == '@':
            return NodeKind.entrance
        char_num = ord(symbol)
        if char_num >= 65 and char_num <= 90:
            return NodeKind.door
        elif char_num >= 97 and char_num <= 122:
            return NodeKind.key

class Karta:
    def __init__(self, file_path: str):
        self.karta      : list[list[TunnelNode]]      = []
        self.keys       : list[TunnelNode]            = []
        self.doors      : list[TunnelNode]            = []
        self.positions  : dict[TunnelNode:Coordinate] = dict()
        self.entrances  : list[TunnelNode]            = []

        with open(file_path) as puzzle_input:
            entrace_nr = 0
            for y,line in enumerate(puzzle_input):
                row = []
                self.karta.append(row)
                for x,symbol in enumerate(line.strip()):
                    node = TunnelNode(symbol,TunnelNode.kind(symbol))
                    self.positions[node] = Coordinate(x,y)
                    row.append(node)
                    if node.am_key():
                        self.keys.append(node)
                    if node.am_door():
                        self.doors.append(node)
                    if node.am_entrance():
                        node.name = str(entrace_nr)
                        entrace_nr += 1
                        self.entrances.append(node)

        self.aquaint()

    def aquaint(self):
        for node in self.iterator():
            for neighbour in self.getSurroundings(self.positions[node]):
                node.addNearNode(neighbour,1)

    def print(self):
        for row in self.karta:
            for node in row:
                print(node.name,end='')
            print()
    
    def at(self,position: Coordinate):
        try:
            node = self.karta[position.y][position.x]
            if node.name == '#':
                return False
            return node
        except IndexError:
            return False
    
    def getSurroundings(self,position: Coordinate):
        surroundings = []
        for step in [Coordinate(-1,0),Coordinate(1,0),Coordinate(0,-1),Coordinate(0,1)]:
            coordinate = position + step
            node = self.at(coordinate)
            if node:
                surroundings.append(node)
        return surroundings

    def iterator(self):
        return (item for it in self.karta for item in it)
    
    def print_keys(self):
        for i,key in enumerate(self.keys):
            print(i,key.name,self.positions[key])
    
    def print_doors(self):
        for i,door in enumerate(self.doors):
            print(i,door.name,self.positions[door])

class KeyRegister:
    def __init__(self,karta: Karta, multithreaded = False) -> None:
        self.karta              : Karta                                                     = karta
        self.register           : defaultdict[str,dict[str,tuple(int,int)]]                 = defaultdict(lambda: dict())
        self.key_binary_dict    : dict[str,int]                                             = {key.name : 1 << i for i,key in enumerate(self.karta.keys)}
        self.all_keys           : int                                                       = int('0b'+'1'*len(self.key_binary_dict),2)
        self.process_distances(multithreaded)

    def process_distances(self,multithreaded) -> None:

        node_connections: list[tuple[TunnelNode,list[TunnelNode]]] = []
        
        for i,key_from in enumerate(self.karta.keys[:-1]):
            node_connections.append( (key_from,self.karta.keys[i+1:]) )
        
        for entrance in self.karta.entrances:
            node_connections.append( (entrance,self.karta.keys) )

        if multithreaded:
            with Pool() as pool:
                all_paths = pool.starmap(TunnelNode.pathsFromTo,node_connections)
        else:
            all_paths = [TunnelNode.pathsFromTo(*connections) for connections in node_connections]
        
        paths: list[list[TunnelNode]] = sum(all_paths,[])
        
        for path in paths:
            keys_bit_mask = sum(self.key_binary_dict[node.name.lower()] for node in path if node.am_door())
            self.register[path[0].name][path[-1].name] = (keys_bit_mask,len(path)-1)
            if not path[0].am_entrance():
                self.register[path[-1].name][path[0].name] = (keys_bit_mask,len(path)-1)

    def print_register(self):
        for key_from in self.register:
            print(key_from)
            for destination,combination in self.register[key_from].items():
                print(' ',destination,'{0:b}'.format(combination[0]),combination[1])

    def print_keys(self):
        for key,binary in self.key_binary_dict.items():
            print(key,'{:b}'.format(binary).zfill(len(self.key_binary_dict)))

### Breadth first search ###

def get_options(position: str, keys: int,register: 'KeyRegister') -> list[tuple[str,int]]:
    
    options = []
    for destination,combination in register.register[position].items():
        # Continue if we already have the key
        if register.key_binary_dict[destination] & keys > 0:
            continue
        # Add to options if we have all required keys
        if combination[0] & keys == combination[0]:
            options.append( ( destination , combination[1] ) )

    return options

def get_steps_bfs(start_nodes: list[TunnelNode], register: KeyRegister) -> int:

    value_sorted_dict = ValueSortedDict([((tuple(node.name for node in start_nodes),0),0)])
    visited_nodes = set()

    while(value_sorted_dict):

        current_node_hashes,currentDistance = value_sorted_dict.pop(0)

        current_keys = current_node_hashes[1]

        if current_keys == register.all_keys:
            return currentDistance
        
        visited_nodes.add(current_node_hashes)
        
        for i,current_node in enumerate(current_node_hashes[0]):

            for nextNode,distanceToNextNode in get_options(current_node,current_keys,register):

                next_node_keys = current_keys | register.key_binary_dict[nextNode]
                next_hash = list(copy(current_node_hashes[0]))
                next_hash[i] = nextNode
                next_node_hash = (tuple(next_hash) , next_node_keys)

                if next_node_hash in visited_nodes:
                    continue
                
                new_dist = currentDistance + distanceToNextNode
                if next_node_hash not in value_sorted_dict or new_dist < value_sorted_dict[next_node_hash]:
                    value_sorted_dict[next_node_hash] = new_dist

    return None

def tests(part2: bool, multithreaded: bool):

    test_cases = [
        ('input18test.txt',8),
        ('input18test1.txt',132),
        ('input18test2.txt',136),
        ('input18test3.txt',81),
        ('input18test4.txt',8),
        ('input18test5.txt',24),
        ('input18test6.txt',32),
        ('input18test7.txt',72),
        ('input18.txt',3918),
        ('input18_2.txt',2004),
    ]

    if not part2:
        test_cases = test_cases[:4]
    
    for i,(input_path,solution) in enumerate(test_cases):

        t0 = time.time()

        karta = Karta(os.path.join(__location__, input_path))

        register = KeyRegister(karta,multithreaded=multithreaded)

        t1 = time.time()

        print(i+1,'/',len(test_cases),end=' ')
        answer = get_steps_bfs(karta.entrances,register)
        if answer==solution:
            print('OK','({:.3f}s,{:.3f}s)'.format(t1-t0,time.time() - t1))
        else:
            print('Fail','( {} != {} )'.format(answer,solution))

### Main ###

def main():

    for prt,input_path in enumerate(['input18.txt','input18_2.txt']):
        t0 = time.time()
        karta = Karta(os.path.join(__location__, input_path))

        register = KeyRegister(karta,multithreaded=False)

        print('part',prt+1,'=',get_steps_bfs(karta.entrances,register),'({:.3f}s)'.format(time.time() - t0))

if __name__ == '__main__':
    # cProfile.run('main()',sort='tottime')
    # main()
    tests(part2=True, multithreaded=False)