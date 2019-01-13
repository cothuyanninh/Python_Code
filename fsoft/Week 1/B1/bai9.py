list_temp = [20,18,45,25,23,4,8,3,19,16]
temp = 0
for i in range(len(list_temp)):
	for j in range(len(list_temp)):
		if list_temp[i] < list_temp[j]:
			temp = list_temp[i] 
			list_temp[i] = list_temp[j]
			list_temp[j] = temp

print(list_temp)

