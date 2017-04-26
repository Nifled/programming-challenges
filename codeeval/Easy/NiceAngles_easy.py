# https://www.codeeval.com/open_challenges/160/
# Nice Angles

# CHALLENGE DESCRIPTION:

# Write a program that outputs the value of angle, reducing 
# its fractional part to minutes and seconds.
test = "0.001"
deg = test.split('.')[0]
mins = (float(test) - int(deg)) * 60
secs = (mins - int(str(mins).split('.')[0])) * 60

print('%d.%02d\'%02d\"' % (int(deg), int(mins), int(secs)))