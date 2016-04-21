# https://www.codeeval.com/open_challenges/156/
# Roller Coaster

# CHALLENGE DESCRIPTION:

# You are given a piece of text. Your job is to write a program that sets the case of text characters according to the following rules:

# 	1. The first letter of the line should be in uppercase.
# 	2. The next letter should be in lowercase.
# 	3. The next letter should be in uppercase, and so on.
# 	4. Any characters, except for the letters, are ignored during determination of letter case.
test = "Whether 'tis nobler in the mind to suffer."
result = ""
temp = 0
for x in test:
    if x.isalpha():
        if temp==0:
            result += x.upper()
            temp = 1
        else:
            result += x.lower()
            temp = 0
    else: 
        result += x
print(result)