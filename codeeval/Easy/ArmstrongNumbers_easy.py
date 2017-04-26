# https://www.codeeval.com/open_challenges/82/
# Armstrong Numbers

# CHALLENGE DESCRIPTION:

# An Armstrong number is an n-digit number that is equal to 
# the sum of the n'th powers of its digits. Determine if the 
# input numbers are Armstrong numbers.

test = "153"
test = test.strip()

result = 0
for x in test:
	result += int(x)**len(test)
print(result == int(test))