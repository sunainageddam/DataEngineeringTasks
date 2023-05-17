"""
Consider a social network with a large 
number of users, where each user is 
represented by a unique ID. Your task is 
to write a function that takes in a set of 
user connections and returns the size of 
the largest group of users who are 
directly or indirectly connected to each 
other.
For example, if the set of connections is 
{(1, 2), (2, 3), (4, 5), (5, 6)}, then there are 
two groups of users: {1, 2, 3} and {4, 5, 
6}, and the function should return 3.
"""

connections = {(1, 2), (2, 3), (4, 5), (5, 6)}

def largest_group(connections):
    groups = []
    for connection in connections:
        group_found = False
        for group in groups:
            if connection[0] in group or connection[1] in group: # [0] - 1, [1] - 2
                group.add(connection[0])
                group.add(connection[1])
                group_found = True
                break
        if not group_found:
            groups.append({connection[0], connection[1]})
    print(groups)    # duplicates are not allowed
    
    max_group_size = 0
    for group in groups:
        group_size = len(group)
        if group_size > max_group_size:
            max_group_size = group_size
    return max_group_size

largestgroup = largest_group(connections)
print(largestgroup)
