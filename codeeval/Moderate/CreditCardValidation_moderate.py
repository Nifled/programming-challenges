# https://www.codeeval.com/open_challenges/172/
# Credit Card Validation

# CHALLENGE DESCRIPTION:

# To check whether a bank card number is valid or it is it 
# just a set of random numbers, Luhn formula is used. Print 
# to stdout the results of bank card numbers validation, one 
# per line. If the number is correct – print 1, 
# otherwise – print 0.
test = "5537 0213 6797 6815" # Example input

y = ''.join(map(str, test.split()))[::-1]
total = 0
for x in range(0,len(y)):
	if x%2 == 1:
		if int(y[x])*2 > 9:
			total += int(y[x])*2 - 9
		else:
			total += int(y[x])*2
	else:
		total += int(y[x])
print('1' if total%10 == 0 else '0')