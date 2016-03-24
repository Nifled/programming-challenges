# https://www.codeeval.com/open_challenges/29/
# Unique Elements

# CHALLENGE DESCRIPTION:

# You are given a sorted list of numbers with duplicates. 
# Print out the sorted list with duplicates removed.
test = '2,3,4,5,5'
listy = list(map(int, test.strip().split(',')))

uniqueList = []
for x in listy:
	if x not in uniqueList:
		uniqueList.append(x)

print(",".join(map(str, uniqueList)))