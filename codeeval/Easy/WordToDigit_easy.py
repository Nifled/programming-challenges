# https://www.codeeval.com/open_challenges/104/
# Word to Digit

# CHALLENGE DESCRIPTION:


# Having a string representation of a set of numbers you 
# need to print this numbers.

# All numbers are separated by semicolon. There are up to 
# 20 numbers in one line. The numbers are "zero" to "nine"
test = "three;seven;eight;nine;two"
result = []
for word in test.strip().split(';'):

	if word == 'zero':
		result.append(0)
	elif word == 'one':
		result.append(1)
	elif word == 'two':
		result.append(2)
	elif word == 'three':
		result.append(3)
	elif word == 'four':
		result.append(4)
	elif word == 'five':
		result.append(5)
	elif word == 'six':
		result.append(6)
	elif word == 'seven':
		result.append(7)
	elif word == 'eight':
		result.append(8)
	elif word == 'nine':
		result.append(9)

print(''.join(map(str, result)))