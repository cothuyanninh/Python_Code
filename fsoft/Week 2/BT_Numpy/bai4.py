import numpy as np 
input_list = np.arange(18).reshape(3,6)
print(input_list.shape)

print(input_list.ndim)

print(input_list.size)

print(input_list.itemsize)

print(input_list.data)

print(np.prod(input_list.shape))

print(input_list.dtype)