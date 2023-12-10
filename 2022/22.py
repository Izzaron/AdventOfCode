from coordinates import Coordinate,Direction
from enum import Enum
from math import sqrt, cos
from random import randint
import time

input_file = __file__.replace('.py','.txt')
test_file = __file__.replace('.py','test.txt')
harder_input_file = __file__.replace('.py','harder.txt')

class Geometry(Enum):
    FLAT = 1
    CUBIC = 2

class Karta:
    def __init__(self,karta: list[list[str]]) -> None:
        self.karta  : list[list[str]]    = karta
        self.widths, self.heights = self.prepare_flat(karta)
        self.cubic_transformation = self.init_cubic_transformation()
        self.pixels_per_edge, self.cubic_input_transformation = self.prepare_cubic(karta)

    def prepare_flat(self, karta: list[list[str]]) -> tuple[list[int],list[int]]:
        widths = [row.count('.')+row.count('#') for row in karta]
        max_x_idxs = max([len(row) for row in karta])
        heights = [[row[i] for row in karta if i < len(row)].count('.')+[row[i] for row in karta if i < len(row)].count('#') for i in range(max_x_idxs)]
        return widths, heights

    def prepare_cubic(self, karta: list[list[str]]) -> tuple[int,dict[tuple[int,int],tuple[int,int]]]:
        pixel_tot = sum(row.count('.') + row.count('#') for row in karta)
        pixels_per_side = pixel_tot/6
        pixels_per_edge = int(sqrt(pixels_per_side))

        current_corner = self.first_corner()
        current_transform = (0,0)
        cubic_corner_map = dict()
        cubic_input_transformation = self.populate_cubic_input_transformation(current_corner, current_transform, cubic_corner_map, pixels_per_edge)
        self.cubic_side_to_rot = [p[1][1] for p in sorted(cubic_input_transformation.items(),key=lambda x: x[1][0])]
        self.cubic_side_to_corner = [p[0] for p in sorted(cubic_input_transformation.items(),key=lambda x: x[1][0])]
        return pixels_per_edge, cubic_input_transformation
    
    def populate_cubic_input_transformation(self, around_position: Coordinate, current_transform: tuple[int,int], cubic_corner_map: dict[tuple[int,int],tuple[int,int]], pixels_per_edge: int) -> dict[tuple[int,int],tuple[int,int]]:
        cubic_corner_map[around_position.asTuple()] = current_transform
        for angle in [0,90,180,270]:
            neighbouring_position = around_position.getCoordinateInDirection(Direction(angle),pixels_per_edge,True)
            symbol = self.at(neighbouring_position)
            if symbol == None:
                continue
            if neighbouring_position.asTuple() in cubic_corner_map:
                continue
            next_transform = self.cubic_transformation[current_transform[0]][Direction(angle+current_transform[1]).angle]
            next_transform = (next_transform[0],Direction(next_transform[1]+current_transform[1]).angle)
            self.populate_cubic_input_transformation(neighbouring_position,next_transform,cubic_corner_map,pixels_per_edge)
        return cubic_corner_map
        
    def init_cubic_transformation(self) -> list[dict[int,tuple[int,int]]]:
        transformation = [
            {0: (3,270), 90: (5,  0), 180: (1, 90), 270: (2,  0)}, #0
            {0: (2,  0), 90: (0,270), 180: (5,180), 270: (4, 90)}, #1
            {0: (3,  0), 90: (0,  0), 180: (1,  0), 270: (4,  0)}, #2
            {0: (5,180), 90: (0, 90), 180: (2,  0), 270: (4,270)}, #3
            {0: (3, 90), 90: (2,  0), 180: (1,270), 270: (5,  0)}, #4
            {0: (3,180), 90: (4,  0), 180: (1,180), 270: (0,  0)}, #5
        ]
        return transformation
    
    def position_to_transform(self,position: Coordinate) -> tuple[int,int]:
        for coordinates,transform in self.cubic_input_transformation.items():
            if position.x >= coordinates[0] and position.y >= coordinates[1] and position.x < coordinates[0] + self.pixels_per_edge and position.y < coordinates[1] + self.pixels_per_edge:
                return transform
        raise IndexError('Position {} not found in input transform'.format(position))

    def start(self) -> Coordinate:
        y = 0
        for x,symbol in enumerate(self.karta[y]):
            if symbol == '.':
                return Coordinate(x,y)
    
    def first_corner(self) -> Coordinate:
        y = 0
        for x,symbol in enumerate(self.karta[y]):
            if symbol in '.#':
                return Coordinate(x,y)
    
    def at(self, position: Coordinate) -> str:
        if position.y < 0 or position.x < 0 or position.y >= len(self.karta) or position.x >= len(self.karta[position.y]):
            return None
        symbol = self.karta[position.y][position.x]
        if symbol == ' ':
            return None
        elif symbol in '.#':
            return symbol
        else:
            raise ValueError('Unexpected symbol ',symbol)

    def peek(self,from_pos: Coordinate, towards: Direction, geometry: Geometry) -> tuple[Coordinate,Direction]:
        
        new_pos = from_pos.getCoordinateInDirection(towards,flip_y=True)
        new_dir = towards
        
        symbol = self.at(new_pos)

        if symbol == None:
            new_pos,new_dir = self.adjust_position(from_pos, towards, new_pos, geometry)
            symbol = self.at(new_pos)

        if symbol == '.':
            return new_pos,new_dir
        elif symbol == '#':
            return from_pos,towards
        else:
            raise ValueError('Unexpected symbol',symbol)

    def adjust_position(self, from_position: Coordinate, from_direction: Direction, new_position: Coordinate, geometry: Geometry) -> tuple[Coordinate,Direction]:
        if geometry == Geometry.FLAT:
            return self.adjust_flat(from_direction, new_position)
        elif geometry == Geometry.CUBIC:
            return self.adjust_cubic(from_position, from_direction, new_position)
        else:
            raise ValueError('Unexpected geometry {}'.format(geometry))

    def adjust_cubic(self, from_position: Coordinate, from_direction: Direction, new_position: Coordinate) -> tuple[Coordinate,Direction]:
        
        # figure out which side we are on
        old_side,old_rot_adj = self.position_to_transform(from_position)

        # use current side and rotation adjustment for that side to figure out which side we are going to and rotation adjustment for that movement
        new_side,base_rot_adj = self.cubic_transformation[old_side][Direction(from_direction.angle+old_rot_adj).angle]

        # get the rotation adjustment for the new side
        new_rot_adj = self.cubic_side_to_rot[new_side]

        # get the direction we are facing on the new side
        new_direction = Direction(from_direction.angle+old_rot_adj+base_rot_adj-new_rot_adj)

        # get the coordinates we should land on, on the new side, from that sides coordinate system but before adjusting for rotation
        local_x,local_y = new_position.x%self.pixels_per_edge, new_position.y%self.pixels_per_edge
        
        # get the position adjustment from local side-coordinates to global coordinates
        global_x,global_y = self.cubic_side_to_corner[new_side]

        # get the rotation change when moving between the sides
        rotation_change = new_direction-from_direction
        
        # get the new position after adjusting for rotation. The pivot takes into account the size of the side and the size of each pixel
        pivot = Coordinate(self.pixels_per_edge/2-0.5,self.pixels_per_edge/2-0.5)
        adjusted_position = Coordinate(local_x,local_y).rotated(rotation_change,pivot,True)
        
        # the new coorinate is translated back into global coordinates and with int type
        new_coor = Coordinate(int(round(adjusted_position.x)) + global_x,int(round(adjusted_position.y)) + global_y)
        
        return new_coor,new_direction

    def adjust_flat(self, from_direction: Direction, new_position: Coordinate) -> tuple[Coordinate,Direction]:
        if from_direction.angle == 0:
            adjusted_x = new_position.x - self.widths[new_position.y]
            adjusted_y = new_position.y
        elif from_direction.angle == 180:
            adjusted_x = new_position.x + self.widths[new_position.y]
            adjusted_y = new_position.y
        elif from_direction.angle == 90:
            adjusted_x = new_position.x
            adjusted_y = new_position.y + self.heights[new_position.x]
        elif from_direction.angle == 270:
            adjusted_x = new_position.x
            adjusted_y = new_position.y - self.heights[new_position.x]
        else:
            raise ValueError('Unexpected angle',from_direction)
        return Coordinate(adjusted_x,adjusted_y),from_direction

def walk(path: list[str], karta: Karta, geometry: Geometry = Geometry.FLAT) -> tuple[Coordinate,Direction]:
    pos = karta.start()
    facing = Direction(0)
    for command in path:
        if command == 'L':
            facing += 90
        elif command == 'R':
            facing -= 90
        else:
            for _ in range(int(command)):
                candidate_pos,new_dir = karta.peek(pos,facing,geometry)
                if candidate_pos == pos:
                    break
                pos = candidate_pos
                facing = new_dir
    return (pos,facing)

def points_from(position: Coordinate,direction: Direction) -> int:

    angle_to_points = {
        0: 0,
        270: 1,
        180: 2,
        90: 3
    }

    y_points = (position.y+1)*1000
    x_points = (position.x+1)*4
    a_points = angle_to_points[direction.angle]

    return y_points + x_points + a_points

if __name__ == "__main__":

    all_karta_inputs: list[list[list[str]]] = []
    all_paths: list[list[str]] = []

    with open(harder_input_file) as puzzle_input:

        current_karta_input: list[list[str]] = []

        for line in puzzle_input:
            if line[0] in '0123456789LR':
                current_path = line.strip().replace('R',' R ').replace('L',' L ').split()
                all_paths.append(current_path)
                all_karta_inputs.append(current_karta_input)
                current_karta_input = []
            elif line[0] == '\n':
                continue
            else:
                current_karta_input.append(list(line[:-1]))

    start_time = time.time()

    # part 1 (input_file)
    pos,facing = walk(all_paths[0],Karta(all_karta_inputs[0]),Geometry.FLAT)
    print(points_from(pos,facing))

    # part 2 (input_file)
    pos,facing = walk(all_paths[0],Karta(all_karta_inputs[0]),Geometry.CUBIC)
    print(points_from(pos,facing))

    # part 3 (harder_input_file)
    total_sum = 0
    for i in range(len(all_paths)):
        pos,facing = walk(all_paths[i],Karta(all_karta_inputs[i]),Geometry.CUBIC)
        total_sum += points_from(pos,facing)
    print(total_sum)

    print('Elapsed: {}'.format(time.time() - start_time))