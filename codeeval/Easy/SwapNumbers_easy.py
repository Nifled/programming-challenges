# https://www.codeeval.com/open_challenges/196/
# Swap Numbers 

# CHALLENGE DESCRIPTION:

# Write a program that, given a sentence where each word has a 
# single digit positive integer as a prefix and suffix, swaps 
# the numbers while retaining the word in between. Words in the 
# sentence are delimited from each other by a space.
test = "4Always0 5look8 4on9 7the2 4bright8 9side7 3of8 5life5"

swapped = []
for word in test.strip().split():
	temp1 = word[0]
	temp2 = word[-1]
	newword = temp2 + word[1:-1] + temp1
	swapped.append(newword)

print(' '.join(map(str, swapped)))