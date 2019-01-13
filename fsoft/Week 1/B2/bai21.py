def convertTo(string_word):
	for i in range(len(string_word)):
		if (string_word[i] == " " and string_word[i+1] == " "):
			continue
		if (string_word[i] >= "A" and string_word[i] <= "Z"):
			string_word = string_word.replace(string_word[i]," "+string_word[i])
	return string_word

string_input = input("Type: ")
print(convertTo(string_input))