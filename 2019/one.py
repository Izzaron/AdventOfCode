import math

input = open("./input1.txt")


def getFuel(mass):
    return math.floor(mass/3)-2

fuel = 0

for line in input:
    moduleMass = int(line)
    moduleFuel = getFuel(moduleMass)

    fuelFuel = moduleFuel

    while(True):
        fuelFuel = getFuel(fuelFuel)
        if fuelFuel <= 0:
            break
        moduleFuel += fuelFuel

    fuel += moduleFuel

print(fuel)