# https://www.codeeval.com/open_challenges/158/
# Interrupted BubbleSort

# CHALLENGE DESCRIPTION:

# Bubble sort is the simplest algorithm for elements sorting. At each iteration 
# we sequentially compare values of subsequent elements and swap them if necessary.

# Your job is to write a program which finds a state of a given list of positive 
# integer numbers after applying a given count of bubble sort iterations.

test = "54 46 0 34 15 48 47 53 25 18 50 5 21 76 62 48 74 1 43 74 78 29 | 6"

numbers = list(map(int, test.split("|")[0].strip().split(" ")))
limit = int(test.split(" | ")[1])

for x in range(1, len(numbers)):

	for y in range(0, len(numbers) -1):

		if numbers[y + 1] < numbers[y]:
			numbers[y], numbers[y + 1] = numbers[y + 1], numbers[y]

	if limit == x:
		break

print(" ".join(map(str, numbers)))
#For this example, the output should be: 
# 0 15 25 18 34 5 21 46 47 48 48 1 43 50 53 29 54 62 74 74 76 78