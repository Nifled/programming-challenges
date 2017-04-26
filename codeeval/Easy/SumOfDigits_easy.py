# https://www.codeeval.com/open_challenges/21/
# Sum of Digits

# CHALLENGE DESCRIPTION:

# Given a positive integer, find the sum of its constituent digits.

test = "4391" #Example
test = test.strip() #I actually had to strip for the right answer, be careful
					#and add this because you never know when you'll need it.
sum = 0
for x in range(len(test)):
	sum += int(test[x])

print(sum)