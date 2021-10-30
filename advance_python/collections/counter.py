"""
    Counter:
        For fast tallies. Can use it against most iterables like dictionaries, strings, list, tuples.
        
"""

from  collections import Counter
print (Counter('superfluous'))

counter = Counter('superfluous')
print (counter['u'])

print (list(counter.elements()))
print( counter.most_common(2))

counter_one = Counter('superfluous')
print (counter_one)
#Counter({'u': 3, 's': 2, 'l': 1, 'r': 1, 'e': 1, 'o': 1, 'p': 1, 'f': 1})

counter_two = Counter('super')
print(counter_one.subtract(counter_two))
#None

print (counter_one)
