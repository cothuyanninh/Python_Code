"""C1"""
def mean(seq):
	return sum(seq)/len(seq)

def median(seq):
	leng = len(seq) 
	if leng%2 == 0:
		return (seq[leng//2] + seq[leng//2 -1])/2
	else:
		return seq[leng//2]

list_temp = [20,18,23,4,8,7,3,19,16,45]
list_temp.sort()
print(mean(list_temp))
print(median(list_temp))

"""C2"""
import numpy as np 
list_temp = [20,18,23,4,8,7,3,19,16,45]
print("Mean: ", np.mean(list_temp))
print("Meadian: ", np.median(list_temp))