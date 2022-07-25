def StrToIntList(string):
	newList = list(string.split(','))
	for i in range(len(newList)):
		if (newList[i] == ''):
			del newList[i]
		else:
			newList[i] = int(newList[i])
	return newList

def compute(op):
	iPtr = 0
	while iPtr < len(op):
		instruction = str(op[iPtr]).zfill(5)

		if (instruction[-2:] == '99'):
			break

		im1, im2, im3 = iPtr+1, iPtr+2, iPtr+3
		pos1, pos2, pos3 = op[im1],0,0
		if (iPtr < len(op)-4):
			pos2 = op[im2]
			pos3 = op[im3]

		mode = {"p1_0":pos1, "p1_1":im1, "p2_0":pos2, "p2_1":im2, "p3_0":pos3, "p3_1":im3}

		parameter1 = mode['p1_'+instruction[-3]]
		parameter2 = mode['p2_'+instruction[-4]]
		parameter3 = mode['p3_'+instruction[-5]]

		#Addition
		if   (instruction[-2:] == '01'):
			op[parameter3] = op[parameter1] + op[parameter2]
			iPtr += 4

		#Multiplication
		elif (instruction[-2:] == '02'):
			op[parameter3] = op[parameter1] * op[parameter2]
			iPtr += 4

		#User input
		elif (instruction[-2:] == '03'):
			print("Enter input: ")
			op[parameter1] = int(input())
			iPtr += 2

		#Computer output
		elif (instruction[-2:] == '04'):
			print("Opcode output: " + str(op[parameter1]))
			#print("At: " + str(pos1))
			iPtr += 2

		#Jump-If-True
		elif (instruction[-2:] == '05'):
			if op[parameter1] != 0:
				iPtr = op[parameter2]
			else:
				iPtr += 3

		#Jump-If-False
		elif (instruction[-2:] == '06'):
			if op[parameter1] == 0:
				iPtr = op[parameter2]
			else:
				iPtr += 3

		#Less than
		elif (instruction[-2:] == '07'):
			if op[parameter1] < op[parameter2]:
				op[parameter3] = 1
			else:
				op[parameter3] = 0
			iPtr += 4

		#Equals
		elif (instruction[-2:] == '08'):
			if op[parameter1] == op[parameter2]:
				op[parameter3] = 1
			else:
				op[parameter3] = 0
			iPtr += 4

		else:
			print(wtf)
			break
	return op

def main():
	f = open("aoc_input_5_1.txt", "r")
	#f = open("aoc_input_5_2.txt", "r") #test input
	opcodeInput = StrToIntList(f.read())

	assert compute([1,0,0,0,99]) == [2,0,0,0,99]
	assert compute([2,3,0,3,99]) == [2,3,0,6,99]
	assert compute([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
	assert compute([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]
	print("assert pass")
	compute(opcodeInput)

	#print(compute(opcodeInput)[0])

main()
