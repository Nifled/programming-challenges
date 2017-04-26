# https://www.codeeval.com/open_challenges/45/
# Reverse and add

# The problem is as follows: choose a number, reverse its 
# digits and add it to the original. If the sum is not a 
# palindrome (which means, it is not the same number from 
# left to right and right to left), repeat this procedure.
test = "195" #Example
totalReps = 0
temp = int(test)
while True:
	totalReps += 1
	suma = temp + int(str(temp)[::-1])
	temp = suma
	if suma == int(str(suma)[::-1]):
		print(totalReps, suma)
		break