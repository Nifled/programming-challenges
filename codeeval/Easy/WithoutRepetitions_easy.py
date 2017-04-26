# https://www.codeeval.com/open_challenges/173/
# Without Repetitions

# CHALLENGE DESCRIPTION:

# In a given text, if there are two or more identical characters 
# in sequence, delete the repetitions and leave only the first character.

test = "But as he spake he drew the good sword from its scabbard, and smote a heathen knight, Jusssstin of thee Iron Valley."
test = test.strip()
n = len(test)

result = ""
for x in range(n-1):
	if test[x] == test[x+1]:
		continue
	result += test[x]

print(result + test[n-1])