# https://www.codeeval.com/open_challenges/22/
# Fibonacci Series

# CHALLENGE DESCRIPTION:

# The Fibonacci series is defined as: F(0) = 0; F(1) = 1; 
# F(n) = F(n–1) + F(n–2) when n>1. Given an integer n≥0, print out the F(n).
test = "20" #example
limit = int(test.strip())
fibo = [0,1]
if limit >= 2:
	for x in range(2,limit+1):
		fibo.append(int(fibo[x-1])+int(fibo[x-2]))
print(fibo[limit])