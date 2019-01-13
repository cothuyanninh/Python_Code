"""C1"""
from collections import Counter
string1 = "fresher"
string2 = "refresh"
cnt1 = Counter(string1)
cnt2 = Counter(string2)
if cnt1 == cnt2 :
	print("True")
else : 
	print("False")

"""C2"""
def count_infor(string_word):
	list_char = list(set([str(i) for i in string_word]))
	dict_result = {}
	for i in range(len(list_char)):
		dict_result[list_char[i]] = 0
	for char in string_word:
		count = 0
		if char in list_char:
			count += 1
		dict_result[char] += count
	# print(dict_result)
	new_result = sorted(dict_result.items(), key=lambda kv: kv[1])
	return new_result
if count_infor(string1) == count_infor(string2):
	print("True")
else:
	print("False")