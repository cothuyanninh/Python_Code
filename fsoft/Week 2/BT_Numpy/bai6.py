import numpy as np 
list_a = [1,2,3]
list_b = [4,5,6]
list_output = np.concatenate((list_a, list_b), axis =0)
list_output_1 = np.vstack((list_a, list_b))

print(list_output)
print(list_output_1)