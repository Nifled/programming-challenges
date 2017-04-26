# https://www.codeeval.com/open_challenges/205/
# Clean Up The Words

# CHALLENGE DESCRIPTION:

# You have a list of words. Letters of these words are mixed
# with extra symbols, so it is hard to define the beginning 
# and end of each word. Write a program that will clean up 
# the words from extra numbers and symbols.
import re

test = "13What213are;11you-123+138doing7"

cleany = re.sub('[^A-Za-z]+',' ', test)
print(cleany[1:].lower() if cleany[0] == ' ' else cleany.lower())