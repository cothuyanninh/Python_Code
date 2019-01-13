import numpy as np 
A = np.random.randint(1,1001,100)
print("*"*20)
print("A: \n", A)

list_2 = np.random.choice(A, 10)
print("*"*20)
print("10 elements from A: \n", list_2)

B = np.arange(1,51)
print("*"*20)
print("B: \n",B)
for i in range(10):
	np.random.shuffle(B)
	print("B in shuffle times %d: "%(i+1), B)

print("*"*20)
for i in range(5):
	C = np.random.choice(B, 10, replace=True)
	print("10 elements from B could be duplicate times %d: "%(i+1), C)


print("*"*20)
for i in range(5):
	D = np.random.choice(B, 10, replace=False)
	print("10 elements from B with no duplicate times %d: "%(i+1), D)
