# https://www.codeeval.com/open_challenges/76/
# String Rotation

# CHALLENGE DESCRIPTION:
# value_when_true if condition else value_when_false

# You are given two strings. Determine if the second 
# string is a rotation of the first string.
test = "Hello,lloHe"
x = test.split(',')
word1, word2 = x[0].lower(), x[1].lower()
print(sorted(word1) == sorted(word2))
# Stupid codeeval returns everything input as 'False'