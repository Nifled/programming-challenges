# https://www.codeeval.com/open_challenges/24/
# Sum of Integers From File

# CHALLENGE DESCRIPTION:

# Print out the sum of integers read from a file.
import sys

test = "C:\\Users\\Erick\\Desktop\\sum.txt" #Filename example

with open(sys.argv[1], 'r') as input:
    file_object = input.read().strip().splitlines()
    print(sum(int(i) for i in file_object))