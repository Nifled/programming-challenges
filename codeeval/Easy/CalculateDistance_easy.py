# https://www.codeeval.com/open_challenges/99/
# Calculate Distance

# CHALLENGE DESCRIPTION:

# You have coordinates of 2 points and need to find the 
# distance between them.
test = "(47, 43) (-25, -11)"

x1 = int(test.split(') (')[0].split(',')[0][1:])
y1 = int(test.split(') (')[0].split(',')[1].strip())
x2 = int(test.split(') (')[1].split(',')[0])
y2 = int(test.split(') (')[1].split(',')[1].strip()[:-1])

result = ((y2-y1)**2 + (x2-x1)**2)**0.5 # Instead of importing sqrt
print(int(result))