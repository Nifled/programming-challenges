# https://www.codeeval.com/open_challenges/167/
# Read More

# CHALLENGE DESCRIPTION:

# You are given a text. Write a program which outputs its lines according to the following rules:

# -If line length is ≤ 55 characters, print it without any changes.
# -If the line length is > 55 characters, change it as follows:
# ---Trim the line to 40 characters.
# ---If there are spaces ‘ ’ in the resulting string, trim it once again to the last space (the space should be trimmed too).
# ---Add a string ‘... <Read More>’ to the end of the resulting string and print it.
test = "Amy Lawrence was proud and glad, and she tried to make Tom see it in her face - but he wouldn't look."
test = test.strip()
if len(test) <= 55:
	print(test)
else:
	test = test[0:40]
	if test.find(' ') != -1:
		test = test[0:test.rfind(' ')]
	print(test + '... <Read More>')