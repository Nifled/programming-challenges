# https://www.codeeval.com/open_challenges/225/
# Testing

# CHALLENGE DESCRIPTION:
# The first argument is a path to a file. Each line includes a 
# test case with two strings separated by a pipeline '|'. The 
# first string is the one the developers provided to you for 
# testing, and the second one is from design.

def check(num):
	if num == 0:
		return 'Done'
	elif num <= 2:
		return 'Low'
	elif num <= 4:
		return 'Medium'
	elif num <= 6:
		return 'High'
	elif num > 6:
		return 'Critical'

test = "Heelo Codevval | Hello Codeeval"
test = test.strip().split(' | ')
dev, des = test[0], test[1]

bugs = 0
for x in range(len(des)):
	if not dev[x] == des[x]:
		bugs += 1

print(check(bugs))