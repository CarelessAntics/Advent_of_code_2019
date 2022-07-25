import math
import numpy

def parseData(data):
	newData = data.splitlines()
	for i in range(len(newData)):
		newData[i] = [j for j in newData[i]]
	return newData

def findAsteroids(data):
	coords = []
	for y in range(len(data)):
		for x in range(len(data[y])):
			if data[y][x] == '#': coords.append((x,y))
	return coords

def vecSub(vecA, vecB):
	return (vecA[0] - vecB[0], vecA[1] - vecB[1])

def distance(vecA, vecB):
	newVec = vecSub(vecA, vecB)
	dist = math.sqrt(newVec[0]*newVec[0] + newVec[1]*newVec[1])
	return dist

def onPath(posA, posB, posC):
	d1 = distance(posA, posC)
	d2 = distance(posC, posB)
	d3 = distance(posA, posB)
	return ((d1 + d2) - d3) <= .0001

def countAsteroids(data):
	LOScounts, index = [], 0
	for a in data:
		LOScounts.append(0)
		for b in data:
			passed = True
			if b != a:
				for c in data:
					if c != a and c != b and onPath(a,b,c):
						passed = False
						break
				if passed: LOScounts[index] += 1
		index += 1
	return LOScounts
	#return LOScounts

def bestSpot(data, counts):
	return data[counts.index(max(counts))]

def rotate2D(vec, a):
	return (vec[0] * math.cos(a) - vec[1] * math.sin(a), vec[0] * math.sin(a) + vec[1] * math.cos(a))

def onHit():
	#march ray in steps, return True or false if hits asteroid radius
	return

def cartesianToPolar(coord):
	deg = math.atan2(coord[1], coord[0])
	dst = distance((0,0), coord)
	return (deg, dst)

def polarToCartesian(coord, o):
	x = coord[1] * math.cos(coord[0]) + o[0]
	y = coord[1] * math.sin(coord[0]) + o[1]
	x, y = int(round(x)), int(round(y))
	return (x, y)

def convertCoords(data, o):
	newData = []
	data.remove(o)
	for d in data:
		polarVec = vecSub(d, o)
		newData.append(cartesianToPolar(polarVec))
	newData.sort(key=lambda tup: tup[0])
	return newData

def megaLaser(asteroids, o):
	herp = None
	count = 0
	asteroidDict = {}
	a = math.atan2(-1, 0)
	angles = sorted(list(set([i[0] for i in asteroids])))
	#angles.reverse()
	aIndex = angles.index(a)
	for n in angles:
		asteroidDict[n] = [x for x in asteroids if x[0] == n]
	while len(asteroids) > 0:
		if asteroidDict[a]:
			doomedAsteroid = (min(asteroidDict[a], key=lambda tup: tup[1]))
			aIndex = aIndex + 1 if aIndex + 1 < len(angles) else 0
		else:
			aIndex = aIndex + 1 if aIndex + 1 < len(angles) else 0
			a = angles[aIndex]
			continue
		destroyed = asteroids.pop(asteroids.index(doomedAsteroid))
		asteroidDict[a].remove(destroyed)
		print(str(count+1) + ': ' + str(polarToCartesian(destroyed, o)))
		count += 1
		if count == 200: herp = polarToCartesian(destroyed, o)

		a = angles[aIndex]

	return herp[0] * 100 + herp[1]


'''
def megaLaser(o, asteroids):
	asteroids.remove(o)
	d = (0, -1) #Direction is up
	pos = o
	angle = 0
	count = 0
	maxDist = 50.
	radius = .1
	step = .1
	destroyed = []
	while len(asteroids) > 0:
		for i in numpy.arange(0, maxDist, step):
			pos = (pos[0] + d[0]*step, pos[1] + d[1]*step)
			hitCoord = (round(pos[0]+radius), round(pos[1])) #Figure out the rounding
			if hitCoord in asteroids:
				destroyed.append(asteroids.pop(asteroids.index(hitCoord)))
				print(str(count +1) + ': ' + str(destroyed[count]))
				count += 1
				break


		for a in asteroids:
			if onPath(o, d, a):
				destroyed.append(asteroids.pop(asteroids.index(a)))
				print(str(count +1) + ': ' + str(destroyed[count]))
				count += 1
				break

		d = rotate2D(d, .1)
	return destroyed
	'''



def main():
	f = open("aoc_input_10_1.txt", "r")
	asteroidData = parseData(f.read())
	asteroidCoords = findAsteroids(asteroidData)

	''' part1
	asteroidCounts = countAsteroids(asteroidCoords)
	loc = bestSpot(asteroidCoords, asteroidCounts)
	print(max(asteroidCounts))
	print(loc)
	'''

	#(19, 14), 274, part2
	#megaLaser((11,13), asteroidCoords)
	o = (19,14)
	polarCoords = convertCoords(asteroidCoords, o)
	print(megaLaser(polarCoords, o))
main()