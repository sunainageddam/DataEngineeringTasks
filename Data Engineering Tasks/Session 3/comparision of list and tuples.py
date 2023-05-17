#LISTS
a = [1, 2, 3, 4]
b = [2, 3, 4]

#by using ==, !=, <, > operator  

print(a == b)
print(a!= b)  
print(a < b)  
print(a <= b)  
print(a > b)  
print(a >= b)

# Convert lists to sets for comparison
s1 = set(a)
s2 = set(b)
print(s1 == s2) 
print(s1.union(s2))

# Sort before convert
sorted_a = sorted(a)
sorted_b = sorted(b)
print(sorted_a == sorted_b)

# Use all() to compare all elements
print(all(a == b for a, b in zip(a, b)))

# Use zip() to compare element-wise and find differences
diff = [(a, b) for a, b in zip(a, b) if a != b]
print(diff)

#TUPLES   

#by using ==, !=, <, > operator to compare tuples lexicographically 

a = (1, 2, 3, 4)
b = (3, 4, 2)

print(a == b)
print(a!= b)  
print(a < b)  
print(a <= b)  
print(a > b)  
print(a >= b)

# Convert tuples to sets for comparison
s1 = set(a)
s2 = set(b)
print(s1 == s2) 
print(s1.union(s2))

# Sort before convert
sorted_a = sorted(a)
sorted_b = sorted(b)
print(sorted_a == sorted_b)

# Use all() to compare all elements
print(all(a == b for a, b in zip(a, b)))

# Use zip() to compare element-wise and find differences
diff = [(a, b) for a, b in zip(a, b) if a != b]
print(diff)  


