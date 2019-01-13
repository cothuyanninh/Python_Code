fb = open("example.txt", "r").read().replace(".","").replace(",","")
list_word = list(set(fb.split(" ")))
dict_result = {}
for i in list_word:
	dict_result[i] = 0
for i in list_word:
	if i in fb:
		dict_result[i]+= 1
print(dict_result)