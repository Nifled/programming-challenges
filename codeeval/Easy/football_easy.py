from collections import defaultdict

test = "1 2 3 4 | 3 1 | 4 1"
test = test.split(' | ')

dicty = defaultdict(list)
result = ''

for index, val in enumerate(test):

    tmp = val.split(' ')
    for x in tmp:
        dicty[x].append(index+1)

for key in sorted(dicty):
    result += '{}:{}; '.format(key, dicty[key])

print(result.replace('[', '').replace(']', '').replace(', ', ','))
