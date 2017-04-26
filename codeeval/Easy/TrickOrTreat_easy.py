# https://www.codeeval.com/open_challenges/220/
# Trick or Treat

# CHALLENGE DESCRIPTION:

# Everyone knows what Halloween is and how children love it. Children in 
# costumes travel from house to house asking for treats with a phrase 
# "Trick or treat". After that, they divide the treats equally among all. 
# This year, they collected tons of candies, and need your help to share 
# everything equally. 
# You know that children receive different number of candies depending on 
# their costume: vampire gets 3 candies from one house, zombie – 4 candies, 
# and witch – 5 candies. 
# That is, three children in three different costumes get 3+4+5=12 candies 
# from one house.

import re

test = "Vampires: 1, Zombies: 1, Witches: 1, Houses: 1"
test = re.findall(r'\d+', test)
test = list(map(int, test))

v, z, w, houses = 3, 4, 5, test.pop(3)

summ = v*test[0]*houses + z*test[1]*houses + w*test[2]*houses
div = sum(test)

print(summ//div)