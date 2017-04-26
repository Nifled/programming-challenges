# https://www.codeeval.com/open_challenges/41/
# Array Absurdity

# CHALLENGE DESCRIPTION:

# Imagine we have an immutable array of size N which we know to be filled 
# with integers ranging from 0 to N-2, inclusive. Suppose we know that 
# the array contains exactly one duplicated entry and that duplicate 
# appears exactly twice. Find the duplicated entry. (For bonus points, 
# ensure your solution has constant space and time proportional to N)

test = "20;0,1,10,3,2,4,5,7,6,8,11,9,15,12,13,4,16,18,17,14" #Example

numbers = list(map(int, test.split(";")[1].split(",")))
length = int(test.split(';')[0])

comparable = []

for x in range(0, length-1):
	currentNum = numbers[x]
	comparable = numbers[:x] + numbers[x+1:]

	if currentNum in comparable:
		winner = currentNum

print(winner)