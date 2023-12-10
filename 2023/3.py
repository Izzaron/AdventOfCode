from coordinate import Coordinate
from typing import Dict, List
from dataclasses import dataclass

class Number:

    def __init__(self,number) -> None:
        self.number: int = number
        self.isPartNumber: bool = False

@dataclass
class Symbol:
    symbol: str
    coordinate: Coordinate

coordToNumber: Dict[Coordinate,Number] = dict()
symbols: List[Symbol] = []
numbers: List[Number] = []

f = open('3.txt')

numConstr = ''
numCoords = []
for y,line in enumerate(f.readlines()):
    
    if len(numConstr) > 0:
        number = Number(int(numConstr))
        for coord in numCoords:
            coordToNumber[coord] = number
        numbers.append(number)
        numConstr = ''
        numCoords = []

    for x,c in enumerate(line.strip()):
        if c.isdigit():
            numConstr += c
            numCoords.append(Coordinate(x,y))
            continue
        
        if len(numConstr) > 0:
            number = Number(int(numConstr))
            for coord in numCoords:
                coordToNumber[coord] = number
            numbers.append(number)
            numConstr = ''
            numCoords = []

        if c != '.':
            symbols.append(Symbol(c,Coordinate(x,y)))
f.close()

for symbol in symbols:
    for adj in symbol.coordinate.adjecent():
        if adj in coordToNumber:
            coordToNumber[adj].isPartNumber = True

print(sum([number.number for number in numbers if number.isPartNumber]))

gear_ratio_sum = 0
gears = dict()

for symbol in symbols:
    if not symbol.symbol == '*':
        continue
    adjNums: List[Number] = []
    for adj in symbol.coordinate.adjecent():
        if adj in coordToNumber and coordToNumber[adj] not in adjNums:
            adjNums.append(coordToNumber[adj])
    if len(adjNums) == 2:
        gear_ratio_sum += adjNums[0].number * adjNums[1].number
        gears[symbol.coordinate] = symbol

print(gear_ratio_sum)