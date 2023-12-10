from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Coordinate:
    x: int = 0
    y: int = 0

    def adjecent(self) -> List['Coordinate']:
        adjecents: List['Coordinate'] = list()
        for y in [-1,0,1]:
            for x in [-1,0,1]:
                if x == 0 and y == 0:
                    continue
                adjecents.append(Coordinate(self.x+x,self.y+y))
        return adjecents