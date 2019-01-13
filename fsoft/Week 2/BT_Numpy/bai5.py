import numpy as np 
array_zero_default = np.zeros(10)
array_zero = np.zeros(10, dtype = "int16")
array_one_default = np.ones(10)
array_one = np.ones(10, dtype = "int16")
array_empty_default = np.empty(10)
array_empty = np.empty(10, dtype = "int16")

print(array_one_default)
print(array_zero)

print(array_one_default)
print(array_one)

print(array_empty_default)
print(array_empty)