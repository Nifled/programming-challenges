# https://www.codeeval.com/open_challenges/103/
# Lowest Unique Number

# CHALLENGE DESCRIPTION:

# There is a game where each player picks a number from 1 to 9, 
# writes it on a paper and gives to a guide. A player wins if his 
# number is the lowest unique. We may have 10-20 players in our game.

test = "3 3 9 1 6 5 8 1 5 3"
test = test.strip().split()

counter = {}
for x in test:
	if x not in counter:
		counter[x] = 1
	else:
		counter[x] += 1

temp = []
for x in counter:
	if counter[x] == 1:
		temp.append(int(x))

if temp:
	print(test.index(str(min(temp)))+1)
else: 
	print('0')