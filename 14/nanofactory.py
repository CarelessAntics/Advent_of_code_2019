import math

def isInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def parser(f):
	rawLines = f.read().splitlines()
	dataVals = [x.split(' => ')[0] for x in rawLines]
	dataVals = [[y.split(' ') for y in x.split(', ')] for x in dataVals]
	#dataVals = [x.split(' ') for x in dataVals]
	print(dataVals)
	dataKeys = [x.split(' => ')[1] for x in rawLines]
	dataKeys = [tuple(x.split(' ')) for x in dataKeys]

	data = {}
	for k in range(len(dataKeys)):
		
		print(dataKeys[k])
		data[dataKeys[k]] = dataVals[k]
	print(data)
	return data

def react(data, inv, key, n):
	result = 0
	m = int(key[0])
	print("key: ", end='')
	print(key)
	'''
	if key[1] == 'ORE':
		print("return: ", end='')
		print(m)
		return m
	'''
	keys = list(data.keys())

	for i in data[key]:
		if not key[1] in inv: inv[key[1]] = 0

		rounds = math.ceil(n/m)
		print("rounds: ", end='')
		print(rounds)
		t = 0
		for j in range(rounds):
		#while True:
			#print(inv)
			if inv[key[1]] + t >= n:
				inv[key[1]] -= n - t 
				continue

			#nextKey = tuple(i)
			if i[1] != 'ORE': 
				nextKey = [k for k in keys if k[1] == i[1]][0]
				result += react(data, inv, nextKey, int(i[0]))
			else:
				result += int(i[0])

			t += m
			print("amount generated of " + key[1] + ':', end=' ')
			print(t)
			if t >= n:
				inv[key[1]] += t%n
				t -= t%n
			print(inv)

				

	print("ORE USED: ", end='')
	print(str(result) + '\n')
	return result



def main():
	f = open("aoc_input_14_1.txt", "r")
	chemData = parser(f)
	print(react(chemData, {}, ('1', 'FUEL'), 1))

main()