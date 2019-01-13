import numpy as np 

from collections import Counter
A = np.random.randint(0,5,30)
print("A: ",A)
most_number_and_sqe = Counter(A).most_common(1)
print("Number %d have %d frequent. This is most frequent value!"%(most_number_and_sqe[0][0], most_number_and_sqe[0][1]))

B = np.random.randint(40,101,20)
print("B: ",B)
C = np.unique(B)
C.sort()
print("This is 3 max value in B: %d, %d, %d"%(C[-1], C[-2], C[-3]))

B[B==C[-1]] = -1
print("B affter change max of B into -1: ", B)