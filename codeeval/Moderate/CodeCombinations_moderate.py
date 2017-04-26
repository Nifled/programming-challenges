# https://www.codeeval.com/open_challenges/238/
# Code Combinations

# CHALLENGE DESCRIPTION:

# You need to check whether it is possible to make the word 'code' with a 
# given matrix and the four given letters, and, if possible, count how 
# many times you can do this. Letters can be in a various order.
test = "**** | *co* | *de* | ****"

x = [y.strip() for y in test.split(' | ')]

result = 0
for i in range(len(x)-1):
	for j in range(len(x[0])-1):
		tempMatrix = [x[i][j], x[i+1][j], x[i][j+1], x[i+1][j+1]]

		if  'c' in tempMatrix and 'o' in tempMatrix and \
			'd' in tempMatrix and 'e' in tempMatrix:
			result += 1

print(result)