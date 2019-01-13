"""C1"""
string_word = "Fresher Academy"
for i in range(1,len(string_word)+1):
	print(string_word[-i], end ="")

"""C2"""
string_word = "Fresher Academy"
list_temp = [str(i) for i in string_word]
list_temp.reverse()
print("".join(str(i) for i in list_temp))