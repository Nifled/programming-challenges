# https://www.codeeval.com/open_challenges/19/
# Bit Positions

# CHALLENGE DESCRIPTION:

# Given a number n and two integers p1,p2 determine if the bits in 
# position p1 and p2 are the same or not. Positions p1 and p2 are 1 based.

test = "125,1,2" #has to return false

n = bin(int(test.split(",")[0]))
p1 = int(test.split(",")[1])
p2 = int(test.split(",")[2])

if n[-p1] == n[-p2]:
	print("true")
else :
	print("false")