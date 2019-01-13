"""C1"""
list_temp = [20,18,23,4,8,3,19,16,45,25]
tong = 0
count = 0
for i in list_temp:
	if i % 2 == 0:
		tong += i
		count += 1

print(tong/count)

"""C2"""
from functools import reduce
list_result = [i for i in list_temp if i%2 == 0]
print (reduce(lambda x, y: x + y, list_result) / len(list_result))