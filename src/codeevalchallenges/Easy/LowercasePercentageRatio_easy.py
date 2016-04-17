# https://www.codeeval.com/open_challenges/147/
# Lettercase Percentage Ratio

# CHALLENGE DESCRIPTION:

# Your task is to write a program which determines (calculates) 
# the percentage ratio of lowercase and 
test = "zozkTYe"
l = len(test)
lower = 0
for letter in test:
	if letter.islower():
		lower += 1
p = lower/l
print('lowercase: %.2f uppercase: %.2f' % (p*100, (1-p)*100))