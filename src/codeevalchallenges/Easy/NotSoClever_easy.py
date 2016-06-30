# https://www.codeeval.com/open_challenges/232/
# Not so Clever/ Stupid Sort

# CHALLENGE DESCRIPTION:

# Imagine that you have to arrange items in a certain order: pencils 
# from black to white in a color palette, photographs by the date taken, 
# banknotes from the highest to the lowest, etc. To do this, you 
# definitely don’t need to use the Stupid sort algorithm. 

def StupidSort(nums, iters):
	count, x = 0, 0
	while count < len(nums)-1:
		
		if x == iters:
			break

		if int(nums[count]) > int(nums[count+1]):
			nums[count], nums[count+1] = nums[count+1], nums[count]
			count = 0
			x += 1
			continue
		else: 
			count += 1
	return ' '.join(nums)


test = "5 4 3 2 1 | 2"
test = test.strip().split(' | ')
nums = test[0].split()

print(StupidSort(nums, int(test[1])))