import os
from copy import deepcopy
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Sensor:
    def __init__(self,sensor_x: int, sensor_y: int, beacon_x: int, beacon_y: int) -> None:
        self.x          :int = sensor_x
        self.y          :int = sensor_y
        self.beacon_x   :int = beacon_x
        self.beacon_y   :int = beacon_y
        self.range      :int = abs(beacon_x-sensor_x) + abs(beacon_y-sensor_y)
    
    def distance_to(self,other,y=None):
        if y != None:
            return abs(other-self.x) + abs(y-self.y)
        return abs(other.x-self.x) + abs(other.y-self.y)

    def in_range(self, x: int, y: int) -> bool:
        return (abs(self.x - x) + abs(self.y - y)) <= self.range

    def borders_with(self, other: 'Sensor') -> list[tuple[int,int]]:

        if self.distance_to(other) > self.range+other.range+1:
            return []

        l,r = sorted([self,other],key=lambda x: x.x)
        p_x = l.x
        p_y = l.y + l.range+1
        while(r.distance_to(p_x,p_y) != r.range+1 and p_y>l.y):
            p_x += 1
            p_y -= 1
        p1 = (p_x,p_y)
        p_x = l.x
        p_y = l.y - l.range-1
        while(r.distance_to(p_x,p_y) != r.range+1 and p_y<l.y):
            p_x += 1
            p_y += 1
        p2 = (p_x,p_y)
        return [p1,p2]

    def __str__(self) -> str:
        return '({},{})->({},{})'.format(self.x,self.y,self.beacon_x,self.beacon_y)
    
    def __repr__(self) -> str:
        return self.__str__()

class Karta:
    def __init__(self, sensors: list[Sensor], beacons: list[tuple[int,int]]) -> None:
        self.min_x = min([s.x for s in sensors] + [b[0] for b in beacons])
        self.min_y = min([s.y for s in sensors] + [b[1] for b in beacons])
        self.max_x = max([s.x for s in sensors] + [b[0] for b in beacons])
        self.max_y = max([s.y for s in sensors] + [b[1] for b in beacons])
        self.karta = [['.' for _ in range(self.min_x,self.max_x+1)] for _ in range(self.min_y,self.max_y+1)]
        for b in beacons:
            self.karta[b[1]-self.min_y][b[0]-self.min_x] = 'B'
        for s in sensors:
            self.karta[s.y-self.min_y][s.x-self.min_x] = 'S'
            
    def print(self) -> None:
        for row in self.karta:
            for square in row:
                print(square,end='')
            print()
    
    def print_sensors(self,sensor1: Sensor, sensor2: Sensor, points: list[tuple[int,int]] = []) -> None:
        karta = deepcopy(self.karta)
        for j in range(len(karta)):
            for i in range(len(karta[j])):
                x = i+self.min_x
                y = j+self.min_y
                if (x == sensor1.x and y == sensor1.y):
                    karta[j][i] = 'O'
                    continue
                if (x == sensor2.x and y == sensor2.y):
                    karta[j][i] = 'G'
                    continue
                s1_in_range = sensor1.in_range(x,y)
                s2_in_range = sensor2.in_range(x,y)
                if s1_in_range:
                    if s2_in_range:
                        karta[j][i] = '&'
                    else:
                        karta[j][i] = '1'
                elif s2_in_range:
                    karta[j][i] = '2'
        for p in points:
            karta[int(p[1])-self.min_y][int(p[0])-self.min_x] = 'X'
        for row in karta:
            for square in row:
                print(square,end='')
            print()

if __name__ == '__main__':
    sensors: list[Sensor] = []
    beacons: list[tuple[int,int]] = []
    with open(os.path.join(__location__, 'input15.txt')) as puzzle_input:
        for ln in [line.split() for line in puzzle_input]:
            sensor_x = int(ln[2].replace('x=','').replace('y=','').replace(',','').replace(':',''))
            sensor_y = int(ln[3].replace('x=','').replace('y=','').replace(',','').replace(':',''))
            beacon_x = int(ln[8].replace('x=','').replace('y=','').replace(',','').replace(':',''))
            beacon_y = int(ln[9].replace('x=','').replace('y=','').replace(',','').replace(':',''))
            sensors.append(Sensor(sensor_x,sensor_y,beacon_x,beacon_y))
            beacons.append((beacon_x,beacon_y))
    
    # sensor1 = sensors[11]#3
    # sensor2 = sensors[6]#9
    # points = sensor1.borders_with(sensor2)
    # karta = Karta(sensors,beacons)
    # karta.print_sensors(sensor1,sensor2,points)

    bound = 4000000

    # #find all points 1+range from each sensor
    poi = set()
    for i in range(len(sensors)):
        for j in range(i+1,len(sensors)):
            for point in sensors[i].borders_with(sensors[j]):
                if point[0] > 0 and point[1] > 0 and point[0] <= bound and point[1] <= bound:
                    poi.add(point)

    # print(poi)
    # print()

    # #discard all points within reach from any sensor
    to_discard = set()
    for p in poi:
        for sensor in sensors:
            if sensor.in_range(p[0],p[1]):
                to_discard.add(p)
                break
    poi.difference_update(to_discard)
    print(poi)
    print(list(poi)[0][0]*4000000+list(poi)[0][1])