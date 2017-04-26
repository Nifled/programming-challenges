# https://www.codeeval.com/open_challenges/10/
# Mth To Last Element

# CHALLENGE DESCRIPTION:

# Write a program which determines the Mth to the 
# last element in a list.
test = "a b c d 4" # Test input

mth = int(test.split()[-1])-1
letters = list(reversed(test.split()))[1:]

try:
    print(letters[mth])
except IndexError:
	pass