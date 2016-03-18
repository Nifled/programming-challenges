# https://www.codeeval.com/open_challenges/19/
# Bit Positions

# CHALLENGE DESCRIPTION:

# Given a number n and two integers p1,p2 determine if the bits in 
# position p1 and p2 are the same or not. Positions p1 and p2 are 1 based.

line = "86,2,3" # Example

n = bin(int(line.split(",")[0]))
p1 = int(line.split(",")[1])
p2 = int(line.split(",")[2])

if n[-p1] == n[-p2]:
	print("true")
else :
	print("false")