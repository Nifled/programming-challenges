# https://www.codeeval.com/open_challenges/30/
# Set Intersection

# CHALLENGE DESCRIPTION:

# You are given two sorted list of numbers (ascending order). The 
# lists themselves are comma delimited and the two lists are semicolon 
# delimited. Print out the intersection of these two sets.
test = "7,8,9;8,9,10,11,12"
list1 = list(map(int, test.split(';')[0].split(',')))
list2 = list(map(int, test.split(';')[1].split(',')))

if list2[0]not in list1:
  print('empty line')
else:
  intersection = []

  for x in list1:
    for y in list2:
      if x == y:
        intersection.append(x)
  print(",".join(map(str, intersection)))