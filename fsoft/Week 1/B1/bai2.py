"""C1"""
list_temp = [20, 18, 23, 4, 8, 3, 19, 16, 45, 25]
max_ = list_temp[0]
min_ = list_temp[0]
for i in list_temp:
	if (i >= max_):
		max_ = i
	if (i <  min_):
		min_ = i
print("MAx: %d"%max_)
print("Min: %d"%min_)

"""C2"""
list_temp = [20, 18, 23, 4, 8, 3, 19, 16, 45, 25]
print("Max is: ", max(list_temp))
print("Min is: ", min(list_temp))