# https://www.codeeval.com/open_challenges/113/
# Multiply Lists

# CHALLENGE DESCRIPTION:

# You have 2 lists of positive integers. Write a program which 
# multiplies corresponding elements in these lists.
test = "13 4 15 1 15 5 | 1 4 15 14 8 2" #Example
list1 = test.split('|')[0].split()
list2 = test.split('|')[1].split()

result = []

for x in range(0,len(list1)):
	for y in range(0,len(list2)):
		if x == y:
			result.append(int(list1[x])*int(list2[y]))
print(' '.join(map(str, result)))