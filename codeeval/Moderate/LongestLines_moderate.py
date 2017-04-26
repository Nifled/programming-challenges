# https://www.codeeval.com/open_challenges/2/
# Longest Lines

# CHALLENGE DESCRIPTION:

# Write a program which reads a file and prints to stdout the specified 
# number of the longest lines that are sorted based on their length in 
# descending order.

test_cases = open(sys.argv[1], 'r')

lines = [i.rstrip() for i in test_cases]
num = int(lines[0]) # Every file has sort-based number on first line.

print('\n'.join(sorted(lines, key=len)[:num+1:-1]))