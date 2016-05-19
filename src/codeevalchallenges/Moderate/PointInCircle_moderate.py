# https://www.codeeval.com/open_challenges/98/
# Point in Circle 

# CHALLENGE DESCRIPTION:

# Having coordinates of the center of a circle, it's radius 
# and coordinates of a point you need to define whether this 
# point is located inside of this circle.
def pointInCircle(point, center, radius):
	p_xy = list(map(float, point.split(', '))) 
	c_xy = list(map(float, center.split(', ')))
	d = ((p_xy[0] - c_xy[0])**2 + (p_xy[1] - c_xy[1])**2 )**0.5

	if d < float(radius):
		return 'true'
	return 'false'


# Codeeval example
test = "Center: (-9.86, 1.95); Radius: 47.28; Point: (6.03, -6.42)"

split = test.split(';')

center = split[0][split[0].find('(')+1 : split[0].find(')')]
radius = split[1][9:]
point = split[2][split[2].find('(')+1 : split[2].find(')')]

print(pointInCircle(point, center, radius))