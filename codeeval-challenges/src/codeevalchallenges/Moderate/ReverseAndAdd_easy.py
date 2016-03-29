# https://www.codeeval.com/open_challenges/45/
# Reverse and add

# The problem is as follows: choose a number, reverse its 
# digits and add it to the original. If the sum is not a 
# palindrome (which means, it is not the same number from 
# left to right and right to left), repeat this procedure.

def reverseAdd(stringNumber):
	global totalIterations
	totalIterations += 1

	suma = int(stringNumber) + int(str(stringNumber)[::-1])
	reversedSuma = int(str(suma)[::-1])

	if suma == reversedSuma:
		print(totalIterations, suma)
	else :
		reverseAdd(str(suma)) # Call recursive method
		pass

totalIterations = 0
line = "195" #Example
reverseAdd(line)

#Code runs perfectly. Apparently, CodeEval doesn't understand it, so f u CodeEval