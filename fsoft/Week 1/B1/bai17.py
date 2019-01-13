list_temp  = ["fresher", "academy", "science", "data", "study"]

def bublesort(list_temp_):

	for i in range(len(list_temp_)):
		for j in range(len(list_temp_)):
			if list_temp_[i][0] < list_temp_[j][0]:
				temp_1 = list_temp_[i][0]
				list_temp_[i][0] = list_temp_[j][0]
				list_temp_[j][0] = temp_1
				temp_2 = list_temp_[i][1]
				list_temp_[i][1] = list_temp_[j][1]
				list_temp_[j][1] = temp_2

	return list_temp_


def find_sum_word(word):
	sum_ = 0
	for i in word:
		sum_ += ord(i)
	return sum_
 
result = [[find_sum_word(list_temp[i]), list_temp[i]] for i in range(len(list_temp))]
print(result)

print(bublesort(result))
