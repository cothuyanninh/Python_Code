"""C1"""
string1 = "Fresher Academy"
string2 = "data science"

# Cap1
def CapFirst(char):

	if char >= "A" and char <= "Z":
		return char
	elif char >= "a" and char <= "z":
		return chr(ord(char) -32)
	else :
		return char

def Uncap(char):
	if char >= "A" and char <= "Z":
		char = chr(ord(char) +32)
		return char
	else :
		return char

def Cap(char):
	if char >= "a" and char <= "z":
		char = chr(ord(char) -32)
		return char
	elif char >= "A" and char <= "Z":
		return char
	else:
		return char

string1= string1.replace(string1[0], CapFirst(string1[0]))

for i in range(len(string1)- 1):
	if string1[i] == " ":
		string1 = string1.replace(string1[i+1], Uncap(string1[i+1]))
		# string1[i+1] = Uncap(string1[i+1])
print(string1)

# Cap2
string2= string2.replace(string2[0], CapFirst(string2[0]))
for i in range(len(string2) -1):
	if (string2[i]) == " ":
		string2 = string2.replace(string2[i+1], Cap(string2[i+1]))

print(string2)

"""C2"""
string1 = "Fresher Academy"
string2 = "data science"
print(string1.capitalize())
print(string2.title())