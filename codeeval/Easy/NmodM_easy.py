# https://www.codeeval.com/open_challenges/62/
# N Mod M

# CHALLENGE DESCRIPTION:

# Given two integers N and M, calculate N Mod M (without using any inbuilt modulus operator).
test = "74,4"

N = int(test.split(',')[0])
M = int(test.split(',')[1])

if N > M or N==M:
    print(N-M*int(str(float(N/M)).split('.')[0])) #Gets left side of division. E.G.(5/2 = 2)
else:
    print(N)