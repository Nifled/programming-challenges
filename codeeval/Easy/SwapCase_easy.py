# https://www.codeeval.com/open_challenges/96/
# Swap Case

# CHALLENGE DESCRIPTION:

# Write a program which swaps letters' case in a sentence. All 
# non-letter characters should remain the same.

test = "JavaScript language 1.8"

result = ""
for x in test.strip():
	if x.isalpha():
		x = x.lower() if x.isupper() else x.upper()
		result += x
		continue
	result += x
print(result)