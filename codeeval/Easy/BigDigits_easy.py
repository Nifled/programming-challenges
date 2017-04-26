# https://www.codeeval.com/open_challenges/163/
# Big Digits

# In this challenge you're presented with a situation in which you 
# need to output big symbols on devices which only support ASCII 
# characters and single, fixed-width fonts. To do this you're going 
# to use pseudo-graphics to ‘draw’ these big symbols.

# Each pixel is marked either with asterisk ‘*’ or with 
# minus ‘-’. Size of a digit is 5×6 pixels.

# Your task is to write a program, which outputs the numbers 
# given to you with the font as in the example.

dictNums = {
	
	0: ['-**--'
	   ,'*--*-', 
		'*--*-', 
		'*--*-', 
		'-**--',
		'-----'],

	1: ['--*--',
		'-**--', 
		'--*--', 
		'--*--', 
		'-***-',
		'-----'],

	2: ['***--',
		'---*-', 
		'-**--', 
		'*----', 
		'****-',
		'-----'],

	3: ['***--',
		'---*-', 
		'-**--', 
		'---*-', 
		'***--',
		'-----'],

	4: ['-*---',
		'*--*-', 
		'****-', 
		'---*-', 
		'---*-',
		'-----'],

	5: ['****-',
		'*----', 
		'***--', 
		'---*-', 
		'***--',
		'-----'],

	6: ['-**--',
		'*----', 
		'***--', 
		'*--*-', 
		'-**--',
		'-----'],

	7: ['****-',
		'---*-', 
		'--*--', 
		'-*---', 
		'-*---',
		'-----'],

	8: ['-**--',
		'*--*-', 
		'-**--', 
		'*--*-', 
		'-**--',
		'-----'],

	9: ['-**--',
		'*--*-', 
		'-***-', 
		'---*-', 
		'-**--',
		'-----']
}

test = "3.1415926"

nums = []
for x in test.strip():
	if x.isdigit():
		nums.append(int(x))


for row in range(6):
	result = ''
	for value in nums:
		result += dictNums[value][row]
	print(result)

# Could've optimized everything but at the time of
# coding this I was really tired...