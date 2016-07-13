# https://www.codeeval.com/open_challenges/40/
# Self Describing Numbers

# CHALLENGE DESCRIPTION:


# A number is a self-describing number when (assuming digit positions 
# 	are labeled 0 to N-1), the digit in each position is equal to 
# the number of times that that digit appears in the number.
# If the number is a self-describing number, print out 1. If not, print out 0.

def count(x, text):
	counter = 0
	for y in text:
		if y == x:
			counter += 1
	return counter


test = "1210"
test = test.strip()

result = '1'
for x in range(len(test)-1):
	tmp = test[x]
	if int(tmp) == count(str(x), test):
		continue
	else:
		result = '0'
		break
print(result)