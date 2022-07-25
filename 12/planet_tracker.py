import itertools
import copy

class Planet:

	def __init__(self, vel, pos, n):
		self.vel = vel
		self.pos = pos		
		self.pot = 0				#potentiaalienergia
		self.kin = 0				#kineettinen energia
		self.tot = 0				#kokonaisenergia
		self.n = n

	def addVec3(self, a, b):
		return [a[0] + b[0], a[1] + b[1], a[2] + b[2]]

	def updatePos(self):
		#self.gravity(other)
		self.pos = self.addVec3(self.pos, self.vel)
		self.pot = self.energy(self.pos)
		self.kin = self.energy(self.vel)
		self.tot = self.kin * self.pot
		#print('pos: ' + str(self.pos) + ' vel: ' + str(self.vel))

	def gravity(self, other):
		#newVel = list(self.vel)
		j = 0
		for i in self.pos:
			#j = self.pos.index(i)
			if other.pos[j] > i:
				self.vel[j] += 1
				other.vel[j] -= 1
			elif other.pos[j] < i:
				self.vel[j] -= 1
				other.vel[j] += 1
			j += 1

		#print(self.vel, end=' ')
		#print(other.vel, end=' ')

	def energy(self, e):
		s = 0
		for i in e: s += abs(i)
		return s

def parseData(f):
	data = f.read().splitlines()
	for d in range(len(data)):
		data[d] = data[d][1:-1].split(', ')
		data[d] = [int(x[2:]) for x in data[d]]
	return data

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a
	
def lcm(a, b):
	return (a*b)/gcd(a,b)

def simStep(obj):
	e = 0
	pPairs = set(itertools.combinations(obj, 2))
	
	for p in pPairs:
		p[0].gravity(p[1])
	#print('')

	for p in obj:
		p.updatePos()
		e += p.tot
	#for p in obj: 
	#	print('pos: ' + str(p.pos) + ' vel: ' + str(p.vel))
	return obj

def simulate(data):
	planets = []
	for i in range(len(data)):
		planets.append(Planet([0,0,0], data[i], i))
	print(data)

	planetcopy = copy.deepcopy(planets)

	steps = 0
	maxSteps = 1000
	initState = []
	initState = [[x.pos[y] for x in planets] for y in range(3)]
	#initState = initState.copy()
	print(initState)
	cycles = []
	for c in range(3):
		cycles.append(1)
		p = copy.deepcopy(planets)
		while True:
			p = simStep(p)
			print([x.pos[c] for x in p])
			#print([x.vel[c] for x in p])
			if [x.pos[c] for x in p] == initState[c] and len(set([x.vel[c] for x in p])) == 1:
				#print(cycles[c])
				break
			cycles[c] += 1
	print(cycles)
	result = int(lcm(cycles[0],lcm(cycles[1],cycles[2])))
	print(result)
	#print([(x.pos, x.vel) for x in t])
	#print([(x.pos, x.vel) for x in h])
	#print([(x.pos, x.vel) for x in planets])
	#print([(x.pos, x.vel) for x in planetcopy])

	#print(mu)
	return



def main():
	f = open("aoc_input_12_1.txt", "r")
	planetData = parseData(f)
	simulate(planetData)
	print(planetData)

main()
