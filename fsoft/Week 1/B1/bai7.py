"""C1"""
import math
output_sum = 0
for i in range(int(math.log(200,2))+ 1):
	output_sum += 2**i
print(output_sum)
"""C2"""
import math
a = [2**i for i in range(int(math.log(200,2)) + 1)]
print(sum(a))