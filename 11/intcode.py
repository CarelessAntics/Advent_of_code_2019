import itertools
import math

def StrToIntList(string):
	newList = list(string.split(','))
	for i in range(len(newList)):
		if (newList[i] == ''):
			del newList[i]
		else:
			newList[i] = int(newList[i])
	return newList

def vecAdd(a, b):
	return (a[0] + b[0], a[1] + b[1])
def vecSub(a, b):
	return (a[0] - b[0], a[1] - b[1])
def rotate2D(vec, a):
	x = (vec[0] * math.cos(a)) - (vec[1] * math.sin(a))
	y = (vec[0] * math.sin(a)) + (vec[1] * math.cos(a))
	return (x, y)

def expandMem(mem, newIndex):
	if (len(mem) < newIndex) & newIndex >= 0:
		addition = newIndex - len(mem)+1
		for i in range(addition):
			mem.append(0)
	return mem

#TODO: make memory a dictionary
def compute(op, iPtr, relBase, *args):
	args = args
	userInput = args[0]
	argIndex = 0
	output = None
	#iPtr = iPtr
	#relBase = relBase
	mem = op.copy()
	if type(mem) is not dict: mem = dict(enumerate(op))
	overflow = False
	while iPtr < len(mem):
		instruction = str(mem[iPtr]).zfill(5)

		if (instruction[-2:] == '99'):
			print('stopped')
			return [mem, output, 'stopped', relBase]

		im1, im2, im3 = iPtr+1, iPtr+2, iPtr+3
		pos1, pos2, pos3 = mem[im1], mem[im2], mem[im3]
		rpos1, rpos2, rpos3 = pos1 + relBase, pos2 + relBase, pos3 + relBase

		mode = {
		"p1_0":pos1, "p1_1":im1, "p1_2":rpos1, 
		"p2_0":pos2, "p2_1":im2, "p2_2":rpos2,
		"p3_0":pos3, "p3_1":im3, "p3_2":rpos3}

		parameter1 = mode['p1_'+instruction[-3]]
		parameter2 = mode['p2_'+instruction[-4]]
		parameter3 = mode['p3_'+instruction[-5]]

		#biggestPar = max(parameter1, parameter2, parameter3)
		#overflow = biggestPar > len(mem)
		#if overflow: mem = expandMem(mem, biggestPar)

		#Addition
		if   (instruction[-2:] == '01'):
			mem[parameter3] = mem[parameter1] + mem[parameter2]
			iPtr += 4

		#Multiplication
		elif (instruction[-2:] == '02'):
			mem[parameter3] = mem[parameter1] * mem[parameter2]
			iPtr += 4

		#User input
		elif (instruction[-2:] == '03'):
			#print("Enter input: ")
			mem[parameter1] = int(userInput)
			if len(args)-1 > argIndex:
				userInput = str(args[argIndex+1])
				argIndex += 1
			iPtr += 2

		#Computer output
		elif (instruction[-2:] == '04'):
			#print(mem)
			print("opcode output: " + str(mem[parameter1]))
			output = mem[parameter1]
			return [mem, output, iPtr+2, relBase]
			#print("At: " + str(pos1))
			iPtr += 2

		#Jump-If-True
		elif (instruction[-2:] == '05'):
			if mem[parameter1] != 0:
				iPtr = mem[parameter2]
			else:
				iPtr += 3

		#Jump-If-False
		elif (instruction[-2:] == '06'):
			if mem[parameter1] == 0:
				iPtr = mem[parameter2]
			else:
				iPtr += 3

		#Less than
		elif (instruction[-2:] == '07'):
			if mem[parameter1] < mem[parameter2]:
				mem[parameter3] = 1
			else:
				mem[parameter3] = 0
			iPtr += 4

		#Equals
		elif (instruction[-2:] == '08'):
			if mem[parameter1] == mem[parameter2]:
				mem[parameter3] = 1
			else:
				mem[parameter3] = 0
			iPtr += 4

		#Relative base offset
		elif (instruction[-2:] == '09'):
			relBase += mem[parameter1]
			iPtr += 2

		else:
			print(wtf)
			break

		#if overflow: op = mem[:-(biggestPar-len(op))]
	return [mem, output, iPtr, relBase]


def amplifierTests(code):
	#l = [0,1,2,3,4]
	l = [5,6,7,8,9]
	combs = list(itertools.permutations(l))
	maxSignal = 0
	#combs = [(4,3,2,1,0)]
	#combs = [(0,1,2,3,4)]
	#combs = [(1,0,4,3,2)]
	#combs = [(9,7,8,5,6)]
	'''
	for c in combs:
		signal = 0
		for n in c:
			signal = compute(code, n, signal)
		maxSignal = max(signal, maxSignal)
	print(signal)
	print(maxSignal)	
	'''
	for c in combs:
		signal = 0
		index = 0
		output = {'ampA':[0,0], 'ampB':[0,0], 'ampC':[0,0], 'ampD':[0,0], 'ampE':[0,0]}

		while True: 
			if index == 0:
				output['ampA'] = compute(code, 0, c[0], 0)
				output['ampB'] = compute(code, 0, c[1], output['ampA'][1])
				output['ampC'] = compute(code, 0, c[2], output['ampB'][1])
				output['ampD'] = compute(code, 0, c[3], output['ampC'][1])
				output['ampE'] = compute(code, 0, c[4], output['ampD'][1])
			else:
				output['ampA'] = compute(output['ampA'][0], output['ampA'][2], output['ampE'][1])
				output['ampB'] = compute(output['ampB'][0], output['ampB'][2], output['ampA'][1])
				output['ampC'] = compute(output['ampC'][0], output['ampC'][2], output['ampB'][1])
				output['ampD'] = compute(output['ampD'][0], output['ampD'][2], output['ampC'][1])
				output['ampE'] = compute(output['ampE'][0], output['ampE'][2], output['ampD'][1])

			if output['ampE'][1] != None:
				signal = output['ampE'][1]
			index += 1
			if output['ampE'][2] == 'stopped':
				break

		maxSignal = max(signal, maxSignal)

	return maxSignal

def robot(data):
	drawing = {(0,0):1}
	pointer = 0
	coord = (0,0)
	output = [None, None, None, None]
	second = False
	d = (0,1)
	relBase	= 0
	while output[2] != 'stopped':
		if coord not in drawing.keys():
			uInput = 0
		else:
			uInput = drawing[coord]
		output = compute(data, pointer, relBase, uInput)
		data = output[0]
		pointer = output[2]
		relBase = output[3]
		if not second:
			drawing[coord] = output[1]
			second = True
		else:
			if output[1] == 0:
				d = rotate2D(d, math.radians(-90))
			elif output[1] == 1:
				d = rotate2D(d, math.radians(90))
			else:
				print('wtf')
			d = (int(round(d[0])), int(round(d[1])))
			coord = vecAdd(coord, d)
			second = False
	return drawing

def printDrawing(data):
	bBox = ((max(data.keys(), key=lambda tup: tup[0])[0], max(data.keys(), key=lambda tup: tup[1])[1]),
		(min(data.keys(), key=lambda tup: tup[0])[0], min(data.keys(), key=lambda tup: tup[1])[1]))
	
	areaSize = vecAdd(bBox[0], bBox[1])
	xDir = 1 if bBox[0][0] < bBox[1][0] else -1
	yDir = 1 if bBox[0][1] < bBox[1][1] else -1
	print(areaSize)
	for y in range(bBox[0][1], bBox[1][1] + 1 * yDir, yDir):
		messageLine = []
		for x in range(bBox[0][0], bBox[1][0] + 1 * xDir, xDir):
			#loc = vecSub((x, y), bBox[0])
			#print(loc)
			if (x,y) not in data: data[(x,y)] = 0
			if data[(x,y)] == 1:
				messageLine.append('#')
			elif data[(x,y)] == 0:
				messageLine.append(' ')
			else:
				messageLine.append('?')
		print(''.join(messageLine))

	return 




def main():
	f = open("aoc_input_11_1.txt", "r")
	#f = open("aoc_input_5_2.txt", "r") #test input
	opcodeInput = StrToIntList(f.read())

	#compute(opcodeInput, 0)
	#print(amplifierTests(opcodeInput))
	#compute(opcodeInput, 0, 2)
	hullPaint = robot(opcodeInput)
	print(len(hullPaint))
	#print(hullPaint)
	printDrawing(hullPaint)

	#print(compute(opcodeInput)[0])

main()
