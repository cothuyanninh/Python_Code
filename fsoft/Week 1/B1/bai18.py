"""C1"""
string_word = "Fresher Academy Data Science".lower()
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
print(new_result[-3:])
"""C2"""
from collections import Counter
import operator

string_word = "Fresher Academy Data Science".lower()
cnt = Counter()
for char in string_word:
	cnt[char] += 1
# print(cnt)
new_result = sorted(dict_result.items(), key=lambda kv: kv[1])
print(new_result[-3:])