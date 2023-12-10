import math

class Coordinate():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,other):
        return Coordinate(self.x + other.x,self.y + other.y)
    
    def __iadd__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self
    
    def __sub__(self,other):
        return Coordinate(self.x - other.x,self.y - other.y)

    def __str__(self):
        return '({},{})'.format(self.x,self.y)
    
    def __repr__(self):
        return '({},{})'.format(self.x,self.y)

    def __eq__(self,other: 'Coordinate'):
        if isinstance(other,Coordinate):
            return self.asTuple() == other.asTuple()
        else:
            return False
    
    def __ne__(self,other):
        return not self.__eq__(other)

    def stepInDirection(self, direction: 'Direction', steps: int = 1):
        self.x += steps * int(math.cos(math.radians(direction.angle)))
        self.y += steps * int(math.sin(math.radians(direction.angle)))
    
    def getCoordinateInDirection(self, direction: 'Direction', steps: int = 1,flip_y: bool = False):
        x = self.x + steps * int(math.cos(math.radians(direction.angle)))
        if flip_y:
            y = self.y - steps * int(math.sin(math.radians(direction.angle)))
        else:
            y = self.y + steps * int(math.sin(math.radians(direction.angle)))
        return Coordinate(x, y)
    
    def asTuple(self):
        return (self.x,self.y)
    
    def direction_to(self,other: 'Coordinate') -> 'Direction':
        return Direction(math.degrees(math.atan2(other.y-self.y,other.x-self.x)))
    
    def taxi_distance_to(self,other: 'Coordinate') -> int:
        return abs(other.x-self.x) + abs(other.y-self.y)
    
    def square_distance_to(self,other: 'Coordinate') -> float:
        return (self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y)
    
    def rotate(self, angle: 'Direction', about: 'Coordinate' = None, flip_y: bool = False):
        self = self.rotated(angle,about,flip_y)

    def rotated(self, angle: 'Direction', about: 'Coordinate' = None, flip_y: bool = False) -> 'Coordinate':

        if not isinstance(about,Coordinate):
            about = Coordinate(0,0)

        if flip_y:
            s = math.sin(math.radians(360-angle.angle))
            c = math.cos(math.radians(360-angle.angle))
        else:
            s = math.sin(math.radians(angle.angle))
            c = math.cos(math.radians(angle.angle))

        adjusted_x = self.x - about.x
        adjusted_y = self.y - about.y

        rotated_x = adjusted_x * c - adjusted_y * s
        rotated_y = adjusted_x * s + adjusted_y * c

        new_x = rotated_x + about.x
        new_y = rotated_y + about.y

        return Coordinate(new_x,new_y)

class Direction():
    def __init__(self, angle: int = 0):
        self.angle = angle % 360
    
    def is_horizontal(self) -> bool:
        return self.angle == 0 or self.angle == 180
    
    def is_vertical(self) -> bool:
        return self.angle == 90 or self.angle == 270
    
    def __add__(self,other):
        if isinstance(other,int):
            sum = self.angle + other
        elif isinstance(other,Direction):
            sum = self.angle + other.angle
        else:
            raise ValueError('unknown type')
        
        return Direction(sum % 360)

    def __sub__(self,other):
        if isinstance(other,int):
            sum = self.angle - other
        elif isinstance(other,Direction):
            sum = self.angle - other.angle
        else:
            raise ValueError('unknown type')
        
        return Direction(sum % 360)
    
    def __eq__(self, other): 
        if isinstance(other,int):
            return self.angle == other
        elif isinstance(other,Direction):
            return self.angle == other.angle
    
    def __str__(self):
        return '{}°'.format(self.angle)
    
    def __repr__(self):
        return '{}'.format(self.angle)