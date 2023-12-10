import math

f = open("/Users/gustaf_holst/Dropbox/Projects/AdventOfCode/2020/Day12input.txt")

# class Boat:
#     def __init__(self):
#         self.x = 0
#         self.y = 0
#         self.direction = 0

#     def move(self,instruction):
#         action = instruction[0]
#         value = int(instruction[1:])
#         if action == "N":
#             self.y += value
#         elif action == "S":
#             self.y -= value
#         elif action == "W":
#             self.x -= value
#         elif action == "E":
#             self.x += value
#         elif action == "L":
#             self.direction = (self.direction + value)%360
#         elif action == "R":
#             self.direction = (self.direction - value)%360
#         elif action == "F":
#             self.x += math.cos(math.radians(self.direction))*value
#             self.y += math.sin(math.radians(self.direction))*value
#         else:
#             print("Invalid action \"{}\"".format(action))
#             exit()
    
#     def getManhattanDistance(self):
#         return abs(self.x) + abs(self.y)

instructions = [line.strip() for line in f]

# ferry = Boat()

# for instruction in instructions:
#     ferry.move(instruction)

# print(ferry.getManhattanDistance())

#Part 2

class WaypointBoat:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.wpx = 10
        self.wpy = 1

    def move(self,instruction):
        action = instruction[0]
        value = int(instruction[1:])
        if action == "N":
            self.wpy += value
        elif action == "S":
            self.wpy -= value
        elif action == "W":
            self.wpx -= value
        elif action == "E":
            self.wpx += value
        elif action == "L":
            for i in range(value/90):
                tmp = self.wpx
                self.wpx = -self.wpy
                self.wpy = tmp
        elif action == "R":
            for i in range(value/90):
                tmp = self.wpx
                self.wpx = self.wpy
                self.wpy = -tmp
        elif action == "F":
            self.x += self.wpx*value
            self.y += self.wpy*value
        else:
            print("Invalid action \"{}\"".format(action))
            exit()
    
    def getManhattanDistance(self):
        return abs(self.x) + abs(self.y)
    
    def printState(self):
        print(self.x)
        print(self.y)
        print(self.wpx)
        print(self.wpy)
        print("")

ferry = WaypointBoat()

for instruction in instructions:
    ferry.move(instruction)
    # print(instruction)
    # ferry.printState()

print(ferry.getManhattanDistance())

#43543 is too high