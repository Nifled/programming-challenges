# https://www.codeeval.com/open_challenges/91/
# Simple Sorting 

# CHALLENGE DESCRIPTION:

# Write a program which sorts numbers.

test = "-29.857 -25.849 -1.157 -33.311 67.590 -37.450 97.293 -33.572 -41.757 -4.338 -19.210"
test = test.split()
numList = [float(x) for x in test]

result = ["%.3f" % num for num in sorted(numList)]
print(' '.join(result))