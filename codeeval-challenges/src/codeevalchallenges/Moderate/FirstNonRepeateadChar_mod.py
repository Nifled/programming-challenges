# https://www.codeeval.com/open_challenges/12/
# First Non-Repeated Character

# CHALLENGE DESCRIPTION:

# Write a program which finds the first non-repeated character in a string.

test = "tooth" #examples

lista = []
for x in range(0,len(test)):
	xString = test[x] #letter that is left out
	without_x = "%s%s" % (test[:x],test[x+1:])

	if xString not in without_x: # checks if the letter that was left out is in the new string
		lista.append(xString)
		
print(lista[0])