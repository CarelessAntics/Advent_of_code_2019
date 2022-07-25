
#Rules: 6 digits, at least one double of a digit, none of the numbers are descending, the double digit is not part of a larger set (at least one set of _only_ 2 identical digits)
def karsija(num_list):
	#Convert the input set to strings, add zeroes if number is <6 digits
	str_set = set([str(n).zfill(6) for n in num_list])

	#Iterate through a copy of the set, check each digit for the other rules
	for i in str_set.copy():
		asc, dbl = False, False
		dbl_list = []
		for j in range(1,6):

			#are the numbers ascending
			if (i[j] >= i[j-1]):
				asc = True
			else:
				asc = False
				break

			#Does any digit appear exactly twice
			#For problem 1, switch == to >=
			if (i.count(i[j]) == 2):
				dbl = True
				#dbl_list.append(i[j])

		#if either condition is not met, remove the entry from the original set
		if not (asc & dbl) : str_set.remove(i)

	return str_set

#Create a set of all the numbers between the input values
def main():
	#puzzle input: 125730-579381
	num = range(125730, 579382)
	pwords = karsija(num)
	print(pwords)
	print(len(pwords))

main()