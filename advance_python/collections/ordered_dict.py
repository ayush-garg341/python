"""
    Ordered dict:
        this dictionary keeps track of the order of the keys as they are added.

"""

d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
print (d)

keys = d.keys()
print (keys)

keys = sorted(keys)
print (keys)

for key in keys:
    print (key, d[key])

from collections import OrderedDict
d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
new_d = OrderedDict(sorted(d.items()))
print (new_d)

for key in new_d:
    print (key, new_d[key])

"""
Note: that if you add new keys, they will be added to the end of the OrderedDict instead of being automatically sorted.
When we compare two orderedDict they will not only test the items for equality, but also that the order is correct.

"""
