# https://www.codeeval.com/open_challenges/102/
# JSON Menu ID's

# CHALLENGE DESCRIPTION:

# You have JSON string which describes a menu. Calculate the SUM of 
# IDs of all "items" in the case a "label" exists for an item.

import re

test = '{"menu": {"header": "menu", "items": [{"id": 70, "label": "Label 70"}, \
		{"id": 85, "label": "Label 85"}, {"id": 93, "label": "Label 93"}, {"id": 2}]}}'


if '"id":' not in test or '"label":' not in test:
	print('0')

else:


	idMatch = re.findall(r'"id": (\d+), "label":', test)

	print(sum(list(map(int, idMatch))))