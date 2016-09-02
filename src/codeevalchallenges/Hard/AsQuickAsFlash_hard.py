# https://www.codeeval.com/open_challenges/239/
# As Quick As A Flash

# We have just received an extremely important information that 
# needs to be sorted. The amount of information is huge, and we 
# need to sort it as soon as possible. That is why we decided to 
# use a quick sort algorithm.

# You need to calculate and print number of pivots in the array 
# during sorting. 

def partition(array, leftIndex, rightIndex):

	pivot = array[leftIndex]
	i = leftIndex
	j = rightIndex

	while i <=j:

		while array[i] < pivot:
			i += 1

		while array[j] > pivot:
			j -= 1

		if i >= j:
			return j
		array[i], array[j] = array[j], array[i]


def quickSort(array, left, right):
	global pivotes

	if left < right:
		x = partition(array, left, right)

		pivotes += 1

		quickSort(array, left, x-1)
		quickSort(array, x+1, right)



pivotes = 0  # pivots in spanish ( ͡° ͜ʖ ͡°)

listy = [5, 2, 6, 1, 3, 4]

quickSort(listy, 0, len(listy) - 1)

print(listy)
print(str(pivotes))