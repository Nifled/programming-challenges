# https://www.codeeval.com/open_challenges/39/
# Happy Numbers

# A happy number is defined by the following process. Starting 
# with any positive integer, replace the number by the sum of 
# the squares of its digits, and repeat the process until the 
# number equals 1 (where it will stay), or it loops endlessly 
# in a cycle which does not include 1. Those numbers for which 
# this process ends in 1 are happy numbers, while those that 
# do not end in 1 are unhappy numbers.

# If the number is a happy number, print out 1. If not, print out 0.
test = "7"

x, trash, happy = int(test), [], 1
while x != 1:
	total = sum([int(i) ** 2 for i in str(x)])
	if total in trash:
		happy = 0
		break
	else:
		trash.append(total)
	x = total
print(happy)