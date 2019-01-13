"""C1"""
import string
list_temp = string.ascii_lowercase + string.ascii_uppercase + string.digits+" "
string_word = "Fresher @cademy"
flag = 0
for i in string_word:
	if i not in list_temp:
		flag = 1

if flag == 1 :
	print("False")
else : 
	print("True")
"""C2"""
string_word = "Fresher @cademy"
flag = 0
for i in string_word:
	if (i!= " "):
		if (i > "A" and i < "z")  == False:
			flag = 1
if (flag == 1):
	print("False")
else:
	print("True")
