# https://www.codeeval.com/open_challenges/202/
# Stepwise Word

# CHALLENGE DESCRIPTION:

# Print the longest word in a stepwise manner.

def maxWord(wordList):

	maxy = wordList[0]
	for x in range(1, len(wordList)):
		if len(wordList[x]) > len(maxy):
			maxy = wordList[x]
	return maxy


test = "cat dog hello"
test = test.split()

bigWord = maxWord(test)

result = []
for x in range(len(bigWord)):
	result.append('*' * x + bigWord[x])

print(' '.join(result))