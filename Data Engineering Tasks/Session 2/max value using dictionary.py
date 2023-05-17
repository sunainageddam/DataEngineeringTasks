""" Write a function that takes a 
dictionary as input and returns the 
key with the maximum value."""

my_dict = {'a': 3, 'b': 6, 'c': 9, 'd': 12}
def max_key(dictionary):
    max_value = max(dictionary.values())
    for key, value in dictionary.items():
        if value == max_value:
            return key
max_key = max_key(my_dict)
print(max_key)

