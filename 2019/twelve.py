import itertools
import copy

from functools import reduce
from math import gcd
import re

def lcm(a, b):
	return int(a * b / gcd(a, b))

def lcms(*numbers):
	return reduce(lcm, numbers)

def gcds(*numbers):
	return reduce(gcd, numbers)

class Moon:
	def __init__(self,name,x,y,z):
		self.name = name
		self.posX = x
		self.posY = y
		self.posZ = z
		self.velX = 0
		self.velY = 0
		self.velZ = 0
		self.startPosX = x
		self.startPosY = y
		self.startPosZ = z
	
	def isBackAtX(self):
		if self.posX == self.startPosX and self.velX == 0:
			return True
		else:
			return False
	
	def isBackAtY(self):
		if self.posY == self.startPosY and self.velY == 0:
			return True
		else:
			return False
	
	def isBackAtZ(self):
		if self.posZ == self.startPosZ and self.velZ == 0:
			return True
		else:
			return False
	
	def __str__(self):
		return self.name + "({},{},{})<{},{},{}>".format(self.posX,self.posY,self.posZ,self.velX,self.velY,self.velZ)
	
	def __repr__(self):
		return self.name + "({},{},{})<{},{},{}>".format(self.posX,self.posY,self.posZ,self.velX,self.velY,self.velZ)

	def __eq__(self,other):
		return self.posX == other.posX and self.posY == other.posY and self.posZ == other.posZ and self.velX == other.velX and self.velY == other.velY and self.velZ == other.velZ
	
	def __ne__(self,other):
		return not self.__eq__(other)
	
	def getPotentialEnergy(self):
		return abs(self.posX) + abs(self.posY) + abs(self.posZ)
	
	def getKineticEnergy(self):
		return abs(self.velX) + abs(self.velY) + abs(self.velZ)

	def feelGravityFrom(self,other):
		if self.posX != other.posX:
			if self.posX > other.posX:
				self.velX -= 1
				other.velX +=1
			else:
				self.velX += 1
				other.velX -=1

		if self.posY != other.posY:
			if self.posY > other.posY:
				self.velY -= 1
				other.velY +=1
			else:
				self.velY += 1
				other.velY -=1

		if self.posZ != other.posZ:
			if self.posZ > other.posZ:
				self.velZ -= 1
				other.velZ +=1
			else:
				self.velZ += 1
				other.velZ -=1

	def move(self):
		self.posX += self.velX
		self.posY += self.velY
		self.posZ += self.velZ

def main():
	puzzleImput = open('input12.txt')
	moonNames = ['Io', 'Europa', 'Ganymede', 'Callisto']

	moons = []

	for i,row in enumerate(puzzleImput):
		
		coordinates = [int(d) for d in re.findall(r'-?\d+', row)]

		moons.append(Moon(moonNames[i],*coordinates))
	
	moonPairs = list(itertools.combinations(moons,2))

	timeStep = 0

	while(timeStep < 1000):
		# print(timeStep)
		# for moon in moons:
		# 	print(moon)
		for moonPair in moonPairs:
			moonPair[0].feelGravityFrom(moonPair[1])
		for moon in moons:
			moon.move()
		timeStep += 1
	
	# print(sum([moon.getPotentialEnergy() * moon.getKineticEnergy() for moon in moons]))

	# part 2
	timeStep = 0

	periodXsetTimes = 0
	periodYsetTimes = 0
	periodZsetTimes = 0
	periodX = 0
	periodY = 0
	periodZ = 0

	while(True):
		for moonPair in moonPairs:
			moonPair[0].feelGravityFrom(moonPair[1])
		for moon in moons:
			moon.move()
		timeStep += 1
		# print(timeStep)

		if periodXsetTimes < 2 and all([moon.isBackAtX() for moon in moons]):
			periodX = timeStep - periodX
			periodXsetTimes += 1
			# print('periodX: ', periodX)
		
		if periodYsetTimes < 2 and all([moon.isBackAtY() for moon in moons]):
			periodY = timeStep - periodY
			periodYsetTimes += 1
			# print('periodY: ', periodY)

		if periodZsetTimes < 2 and all([moon.isBackAtZ() for moon in moons]):
			periodZ = timeStep - periodZ
			periodZsetTimes += 1
			# print('periodZ: ', periodZ)
		
		if periodXsetTimes == 2 and periodYsetTimes == 2 and periodZsetTimes == 2:
			break

	print('periodX: ', periodX)
	print('periodY: ', periodY)
	print('periodZ: ', periodZ)
	print('lcms: ',lcms(periodX,periodY,periodZ))

if __name__ == "__main__":
	main()