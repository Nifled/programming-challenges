# https://www.codeeval.com/open_challenges/115/
# Mixed Content

# CHALLENGE DESCRIPTION:

# You have a string of words and digits divided by comma. 
# Write a program which separates words with digits. You 
# shouldn't change the order elements.

test = "8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21,24,13,14,43,41"
test = test.strip().split(',')

nums = []
words = []
for x in test:
	if x.isnumeric():
		nums.append(x)
	else: 
		words.append(x)
result = ','.join(words) + '|' + ','.join(nums)
if nums and words:
	print(result)
elif nums:
	print(','.join(nums))
else:
	print(','.join(words))