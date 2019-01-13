import math
list_source = [2,3,4,5,7,11,13]

def findX(number):
	if number in list_source:
		return True
	else:
		count = 0
		for i in range(2, int(math.sqrt(number) + 1)):
			if number%i == 0:
				count += 1
		if count == 0:
			return True
print("\n".join(str(x) for x in list_source))
for i in range(13, 101):
	if findX(i):
		print(i)