# Write a program that prints out the final series of numbers 
# where those divisible by X, Y and both are replaced by “F” 
# for fizz, “B” for buzz and “FB” for fizz buzz.

line = "2 7 15"

firstDivider = int(line.split(' ')[0])
secondDivider = int(line.split(' ')[1])

number = int(line.split(' ')[2])

for x in range(1, int(number)+1):
	
	if x%firstDivider == 0 and x%secondDivider == 0:
		print("FB", end = " ")
	elif x%firstDivider == 0 :
		print("F", end = " ")
	elif x%secondDivider == 0 :
		print("B", end = " ")
	else :
		print(x, end = " ")
		pass
print("")

	pass
