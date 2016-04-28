# https://www.codeeval.com/open_challenges/9/
# Stack Implementation

# CHALLENGE DESCRIPTION:

# Write a program which implements a stack interface for 
# integers. The interface should have ‘push’ and ‘pop’ 
# functions. Your task is to ‘push’ a series of integers 
# and then ‘pop’ and print every alternate integer.
class Stack: # Stack Implementation

	def __init__(self):
		self.items = []

	def push(self, number):
		self.items.append(number)

	def pop(self):
		return self.items[-1]

# Due to it being a stack, it should follow the 'First in, Last Out'
test = "10 -2 3 4"
NumsToStack = test.split()[::-1]

stack = Stack() # Instance of my Stack class

result = []
for x in range(len(NumsToStack)):
	stack.push(NumsToStack[x])
	if x%2 == 0: result.append(stack.pop())
print(' '.join(result))