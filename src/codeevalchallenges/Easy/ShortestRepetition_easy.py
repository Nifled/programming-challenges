# https://www.codeeval.com/open_challenges/107/
# Shortest Repetition

# CHALLENGE DESCRIPTION:

# Write a program to determine the shortest repetition in a string. 

import re

test = "abcabcabcabc"	# Example input
test = test.strip()

result = len(test)

r = re.compile(r"(.+?)\1+")
for match in r.finditer(test):
	temp = len(match.group(1))
	if temp < result:
		result = temp
print(result)