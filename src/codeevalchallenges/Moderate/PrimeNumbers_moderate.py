# https://www.codeeval.com/open_challenges/46/
# Prime Numbers

# CHALLENGE DESCRIPTION:

# Print out the prime numbers less than a given number N.  
# You may assume that N is always a positive integer.
def isPrime(number):
	if number<2: return False
	if number>2 and number%2==0: return False

	root = int(number**0.5)
	for x in range(3,root+1,2):
		if number%x == 0:
			return False
	return True


test = "100"

result = ''
for x in range(2,int(test)):
	if isPrime(x): result += str(x) + ','
print(result[:-1])