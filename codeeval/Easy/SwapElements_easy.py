# https://www.codeeval.com/open_challenges/112/
# Swap Elements

# CHALLENGE DESCRIPTION:

# You are given a list of numbers which is supplemented with 
# positions that have to be swapped.

test = "1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3"
test = test.strip().split(' : ')

nums = test[0].split()
for pos in test[1].split(', '):
	x, y = pos.split('-')[0], pos.split('-')[1]
	nums[int(x)], nums[int(y)] = nums[int(y)], nums[int(x)]
print(' '.join(nums))