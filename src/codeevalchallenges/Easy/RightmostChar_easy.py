# https://www.codeeval.com/open_challenges/31/
# Rightmost Char

# CHALLENGE DESCRIPTION:

# You are given a string 'S' and a character 't'. Print out the position 
# of the rightmost occurrence of 't' (case matters) in 'S' or -1 if there 
# is none. The position to be printed out is zero based.
test = "IgqMe0kLZq74sDjfOD2jDcWcjttODlyRixSpzg3HiXS,c"
test = test.strip()

phrase = test.split(',')[0]
chary = test.split(',')[1]
print(str(phrase.rfind(chary)))