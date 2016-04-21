# https://www.codeeval.com/open_challenges/178/
# Matrix Rotation

# CHALLENGE DESCRIPTION:

# You are given a 2D N×N matrix. Each element of the matrix is 
# a letter: from ‘a’ to ‘z’. Your task is to rotate the matrix 
# 90° clockwise:
from math import sqrt

test = "a b c d e f g h i j k l m n o p"

temp = []
li = test.split()
sq = int(sqrt(len(li)))
for x in range(0, len(li), sq):
	temp.append(li[x:x+sq])

result = ""
for x in list(zip(*temp[::-1])):
	for y in x:
		result += y + " "
print(result.strip())