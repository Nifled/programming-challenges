# https://www.codeeval.com/open_challenges/23/
# MULTIPLICATION TABLES

# CHALLENGE DESCRIPTION:

# Print out the grade school multiplication table upto 12*12.

limit = 12
for x in range(1,limit+1):
	for y in range(1,limit+1):
		print('{:4}'.format(x*y), end="") #The {} give it the 4 space format that codeeval wants
	print("")