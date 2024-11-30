# Lists of Lists Initialize
l1 = [['_'] * 3 for x in range(3)]
l2 = [['_']*3]*3

l1[1][1] = 'X' # [['_', '_', '_'], ['_', 'X', '_'], ['_', '_', '_']]
l2[1][1] = 'X' # [['-', 'X', '-'], ['-', 'X', '-'], ['-', 'X', '-']]

# l2 have three same objects from inner list
