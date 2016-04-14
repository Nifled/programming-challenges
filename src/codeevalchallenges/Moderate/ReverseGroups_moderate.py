# https://www.codeeval.com/open_challenges/71/
# Reverse Groups

# CHALLENGE DESCRIPTION:

# Given a list of numbers and a positive integer k, reverse 
# the elements of the list, k items at a time. If the number 
# of elements is not a multiple of k, then the remaining items 
# in the end should be left as is.
test = "1,2,3,4,5,6,7,6,3;1"

numList = list(map(int, test.split(';')[0].split(',')))
k = int(test.split(';')[1])

result = []
for x in range(0,len(numList),k):
	tempList = sorted(numList[x:k+x], reverse=True)
	if len(tempList) < k:
		result += numList[x:]
	else:
		result += tempList
print(','.join(map(str, result)))