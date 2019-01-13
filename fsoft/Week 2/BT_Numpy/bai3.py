import numpy as np 
input_list = np.arange(18)

print(input_list.reshape(3,6))
print(input_list.reshape(6,3))

temp = np.arange(19,22)
ahihi = np.concatenate((input_list, temp))
print(ahihi.reshape(3,7))