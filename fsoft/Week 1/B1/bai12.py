"""C1"""
string_word = "Fresher Academy Ahihi do ngoc"

def split_void(string):
	list_result = []
	id_start = 0
	id_end = 0
	for i in range(len(string)):
		if string[i] == " ":
			id_end = i
			list_result.append(string[id_start:id_end])
			id_start = id_end+1

	for i in range(1, len(string)+1):
		if string[-i] == " ":
			list_result.append(string[-i+1:])
			break

	return list_result
list_ouput = split_void(string_word)
for i in range(1, len(list_ouput)+1):
	print(list_ouput[-i], end =" ")

"""C2"""
string_word = "Fresher Academy Ahihi do ngoc"
string_word = string_word.split(" ")
new_list = []

for i in range(len(string_word)):
	i = i-1
	new_list.append(string_word.pop())
print(" ".join(str(x) for x in new_list))




