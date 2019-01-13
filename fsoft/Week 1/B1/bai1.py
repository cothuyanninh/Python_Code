"""C1"""
for i in range(1901,2031):
	if (i % 5 == 0 and i%13 != 0):
		print(i)

"""C2"""
list_result = [i for i in range(1901, 2031) if (i%5 ==0 and i%13 != 0)]
print("\n".join(str(x) for x in list_result))