# https://www.codeeval.com/open_challenges/93/
# Capitalize Words 

# CHALLENGE DESCRIPTION:

# Write a program which capitalizes the first letter of each word in a sentence.
test = "Hello world"

upper = [x[0].upper() + x[1:] for x in test.split()]

print(" ".join(upper))