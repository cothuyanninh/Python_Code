import numpy as np 
A = np.random.randint(1,51,100)
print("*"*20)
print("A: \n",A)

B = np.unique(A)
print("*"*20)
print("Unique Elements of arrays is B: \n",B)

unique_, counts = np.unique(A, return_counts=True)
result = dict(zip(unique_, counts))
print("*"*20)
print("This is unique elements of the array and occurrences of each element:")
print(result)

final = {key:value for key, value in result.items() if value >= 3}
print("*"*20)
print("Store elements having occurrences larger than 3 into a dictionary: ")
print(final)