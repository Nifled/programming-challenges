# https://www.codeeval.com/open_challenges/132/
# The Major Element

# CHALLENGE DESCRIPTION:

# The major element in a sequence with the length of L is the 
# element which appears in a sequence more than L/2 times. The 
# challenge is to find that element in a sequence.
test = "92,19,19,76,19,21,19,85,19,19,19,94,19,19,22,67,83,19,19,54,59,1,19,19"

numsAndCount = {}
for key in test.strip().split(','):
    if key not in numsAndCount:
        numsAndCount[key] = 1
    else: 
        numsAndCount[key] += 1

#Creates a tuple with highest counts in descending order and '[0]' gets the key or number(19)
highCount = sorted(numsAndCount.items(), key=lambda t:t[1], reverse=True)[0]

lenDiv2 = float(len(test.strip().split(',')))/2
print(highCount[0] if highCount[-1] > lenDiv2 else 'None')