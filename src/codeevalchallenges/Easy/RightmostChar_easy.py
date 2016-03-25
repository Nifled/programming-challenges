# https://www.codeeval.com/open_challenges/31/
# Rightmost Char

# CHALLENGE DESCRIPTION:

# You are given a string 'S' and a character 't'. Print out the position 
# of the rightmost occurrence of 't' (case matters) in 'S' or -1 if there 
# is none. The position to be printed out is zero based.
test = "Oat bT6MJHoyjGWpHYoj8dYE3U3fVry9NRiWK8unxXI6aieWj6kJom4wmgiPqBbva60ZU, " #Just an example
phrase = test.split(',')[0]
chary = test.split(',')[1]

index = []
for x in range(len(phrase)-1,-1,-1):
    if phrase[x] == chary:
        index.append(x)
        break
if len(index) == 0:
    print(-1)
else: 
    print(index[0])