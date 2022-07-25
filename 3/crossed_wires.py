def listPoints(directions):
	points = [(0,0)]
	for d in directions:
		heading = d[0]
		amount = int(d[1:])
		steps = 0
		while steps < amount:
			prev = points[len(points)-1]
			if heading == 'R':
				points.append((prev[0]+1, prev[1]))
			elif heading == 'L':
				points.append((prev[0]-1, prev[1]))
			elif heading == 'U':
				points.append((prev[0], prev[1]+1))
			elif heading == 'D':
				points.append((prev[0], prev[1]-1))
			else:
				print(wtf)
				break
			steps += 1
	return points

def findIntersections(list1, list2):
	intersections = set(list1).intersection(list2)
	intersections.remove((0,0))

	return intersections

def closestDist(positions):
	minDist = float('inf')
	for i in positions:
		minDist = min(minDist, abs(i[0]) + abs(i[1]))
	return minDist

def minSteps(path1, path2, intersections):
	steps = float('inf')
	for i in intersections:
		i1 = path1.index(i)
		i2 = path2.index(i)
		steps = min(steps, i1 + i2)
	return steps


def main():

	#f = open("testinput_3.txt", "r")
	f = open("aoc_input_3_1.txt", "r")
	inputs = f.read().splitlines()
	input1 = inputs[0].split(",")
	input2 = inputs[1].split(",")

	points1 = listPoints(input1)
	points2 = listPoints(input2)

	intersections = findIntersections(points1, points2)
	print(intersections)
	print(closestDist(intersections))
	print(minSteps(points1,points2,intersections))


main()