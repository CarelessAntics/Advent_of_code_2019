def StrToIntList(string):
	newList = list(string.split(','))
	for i in range(len(newList)):
		if (newList[i] == ''):
			del newList[i]
		else:
			newList[i] = int(newList[i])
	return newList

def parse(opcode):
	for i in range(0, len(opcode), 4):
		pos1, pos2, newPos = 0, 0, 0
		if (i < len(opcode)-4):
			pos1 = opcode[i+1]
			pos2 = opcode[i+2]
			newPos = opcode[i+3]
		if (opcode[i]==1):
			opcode[newPos] = opcode[pos1] + opcode[pos2]
		elif (opcode[i]==2):
			opcode[newPos] = opcode[pos1] * opcode[pos2]
		elif (opcode[i]==99):
			break
		else:
			print(wtf)
			break
	return opcode

def GravAssist(opcode):
	testcode = []
	for n in range(100):
		for v in range(100):
			testcode = opcode.copy()
			testcode[1] = n
			testcode[2] = v
			if (parse(testcode)[0] == 19690720):
				print("success")
				return testcode
	return testcode




def main():
	#f = open("aoc_input_2_1.txt", "r")
	f = open("aoc_input_2_2.txt", "r")
	opcodeInput = StrToIntList(f.read())

	assert parse([1,0,0,0,99]) == [2,0,0,0,99]
	assert parse([2,3,0,3,99]) == [2,3,0,6,99]
	assert parse([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
	assert parse([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

	#print(parse(opcodeInput)[0])
	gravList = GravAssist(opcodeInput)
	print(gravList)
	print(100*gravList[1]+gravList[2])

main()
