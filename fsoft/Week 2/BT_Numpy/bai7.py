import numpy as np 
list_a = np.array([1,2,3])
list_b = np.array([4,5,6])

list_out_put = np.concatenate((list_b, list_b), axis =0)
list_output_1 = np.vstack((list_a, list_b))

print(list_out_put)
print(list_output_1)