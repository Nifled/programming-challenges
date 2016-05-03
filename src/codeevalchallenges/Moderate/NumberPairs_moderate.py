# https://www.codeeval.com/open_challenges/34/
# Number Pairs

# CHALLENGE DESCRIPTION:

#  You are given a sorted array of positive integers and a number 'X'. 
#  Print out all pairs of numbers whose sum is equal to X. Print out 
#  only unique pairs and the pairs should be in ascending order.

test = "2,4,5,6,9,11,15;20"
nums = test.strip().split(';')[0].split(',')
suma = int(test.strip().split(';')[1])
result = ''
for x in range(len(nums)):
    for y in range(x+1,len(nums)):
        if int(nums[x]) + int(nums[y]) == suma:
            result += nums[x] + ',' + nums[y] + ';'
print('NULL' if not result else result[:-1])