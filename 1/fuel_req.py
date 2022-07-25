def CalcFuel(m):
	fuel = int(m/3)-2
	if (fuel <= 0):
		return 0
	return CalcFuel(fuel) + fuel

def StrToIntList(string):
	newList = list(string.split('\n'))
	for i in range(len(newList)):
		if (newList[i] == ''):
			del newList[i]
		else:
			newList[i] = int(newList[i])
	return newList

f = open("fuel_req_input.txt", 'r')
aocInput = f.read()
modules = StrToIntList(aocInput)

fuel_total = 0
for m in modules:
	fuel_total += CalcFuel(m)

print(fuel_total)
