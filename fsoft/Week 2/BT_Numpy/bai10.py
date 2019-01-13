import numpy as np 
arr_1 = np.arange(10)
arr_gan = arr_1

arr_copy = arr_1.copy()

arr_view = arr_1.view()

arr_1[4] = 100000
# print(arr_1[4])
# print(type(arr_1))
# print(id(arr_1))
# print(type(arr_copy.dtype))
# print(id(arr_copy))
# print(type(arr_gan.dtype))
# print(id(arr_gan))
# print(type(arr_view.dtype))
# print(id(arr_view))
print(arr_1)
print(arr_gan)
print(arr_copy)
print(arr_view)