
import copy
original_list = [1, 2, [3, 4]]
shallow_copy = copy.copy(original_list)
shallow_copy[2].append(5)
print(original_list)  
print(shallow_copy)


original_list = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original_list)
deep_copy[2].append(5)
print(original_list)  
print(deep_copy)      
