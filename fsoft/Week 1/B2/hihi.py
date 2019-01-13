string_word = "Fresher Academy"
string_word = string_word.split(" ")
for i in range(1, len(string_word)+1):
	print("".join(string_word[-i]), end = " ")
a ="Academy Fresher "
print(a[:-1])