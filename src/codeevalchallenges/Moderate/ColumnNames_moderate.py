# https://www.codeeval.com/open_challenges/197/
# Column Names 

# CHALLENGE DESCRIPTION:

# Microsoft Excel uses a special convention to name its column headers. 
# The first 26 columns use the letters 'A' to 'Z'. Then, Excel names 
# its column headers using two letters, so that the 27th and 28th 
# column are 'AA' and 'AB'. After 'ZZ', Excel uses three letters.

# Write a function that takes as input the number of the column, and 
# returns its header. The input will not ask for a column that would 
# be greater than 'ZZZ'.

def excel(limit):

	for x in range(65, 91):
		limit -= 1
		if limit == 0:
			return(chr(x))

	for x in range(65, 91):
		for y in range(65, 91):
			limit -= 1
			if limit == 0:
				return("%s%s" % (chr(x), chr(y)))

	for x in range(65, 91):
		for y in range(65, 91):
			for z in range(65, 91):
				limit -= 1
				if limit == 0:
					return("%s%s%s" % (chr(x), chr(y), chr(z)))



test = "3702"

test = int(test.strip())
print(excel(test))