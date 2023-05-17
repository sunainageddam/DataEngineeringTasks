""" Count the number of names for each first letter. Using Groupby names
= ['sunaina', 'pranaya', 'srinivas', 'tarun raj', 'tarun ghanta']
Output - {s: 2, p:1, t:2}"""

from itertools import groupby

names = ['sunaina', 'pranaya', 'srinivas', 'tarun raj', 'tarun ghanta']

sorted_names = sorted(names)

groups = groupby(sorted_names, lambda name: name[0])

counts = {}

for key, value in groups:
    count = len(list(value))
    counts[key] = count

print (counts)

