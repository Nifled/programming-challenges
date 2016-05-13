# https://www.codeeval.com/open_challenges/240/
# Mersenne Prime

# CHALLENGE DESCRIPTION:

# Your task is to print all Mersenne numbers that are smaller 
# than the number in a test case. Separate those numbers by commas.
def isPrime(number):
	if number<2: return False
	if number>2 and number%2==0: return False

	root = int(number**0.5)
	for x in range(3,root+1,2):
		if number%x == 0:
			return False
	return True

def isPowerOf2(num):
	powers = []
	for x in range(2,num):
		if 2**x <= num:
			powers.append(2**x)
		else:
			break
	return num in powers


test = "1365"

result = []
for x in range(int(test)):
	if isPrime(x) and isPowerOf2(x+1):
		result.append(x)

print(', '.join(map(str, result)).strip())