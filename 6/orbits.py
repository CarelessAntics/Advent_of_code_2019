def splitOrbits(l):
	return l.split(')')
def firstElement(l):
	return l[0]
def secondElement(l):
	return l[1]
def firstCommon(p1, p2):
	for p in p1:
		if p in p2:
			return p

def crawler(data, root, indCount):
	count = 0
	indCount += 1
	while [d[1] for d in data if d[0] == root] not in [d[0] for d in data]:
		if root in [d[0] for d in data]:
			dataCell = data.pop(data.index([d for d in data if d[0] == root][0]))
			newRoot = dataCell[1]
			count += crawler(data, newRoot, indCount) + indCount +1
		else:
			return count

def reverseCrawler(data, root, path):
	while [d[0] for d in data if d[1] == root] not in [d[1] for d in data]:
		if root in [d[1] for d in data]:
			dataCell = data.pop(data.index([d for d in data if d[1] == root][0]))
			newRoot = dataCell[0]
			path.append(newRoot)
			reverseCrawler(data, newRoot, path)
		else:
			return path

def orbitalTransfers(data):
	path_YOU = reverseCrawler(data.copy(), 'YOU', [])
	path_SAN = reverseCrawler(data.copy(), 'SAN', [])
	node = firstCommon(path_YOU, path_SAN)

	length1 = path_YOU.index(node)
	length2 = path_SAN.index(node)

	return length1 + length2

def main():
	f = open('aoc_input_6_1.txt', 'r')
	orbitList = f.read().splitlines()
	orbitalData = list(map(splitOrbits, orbitList))
	orbitCount = crawler(orbitalData.copy(), 'COM', -1)
	transferCount = orbitalTransfers(orbitalData)

	print("Number of orbits in map: " + str(orbitCount))
	print("Number of orbital transfers: " + str(transferCount))

main()