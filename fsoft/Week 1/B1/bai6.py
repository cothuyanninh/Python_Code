"""C1"""
string_word = "Fresher Academy"
for i in range(len(string_word)):
	if string_word[i] == "a":
		# print("hihi")
		string_word = string_word.replace(string_word[i], "@")
	elif string_word[i] == "e":
		string_word = string_word.replace(string_word[i], "3")
print(string_word)

"""C2"""
string_word = "Fresher Academy"
string_word = string_word.replace("a", "@").replace("e", "3")
print(string_word)