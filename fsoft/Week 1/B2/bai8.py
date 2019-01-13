def displayString(string1, string2):
	if (len(string1) == len(string2)):
		return [string1, string2]
	elif (len(string1) > len(string2)):
		return [string1]
	else:
		return [string2]

string1 = "Fresher AI"
string2 = "Fresher AI HN 01"
print("\n".join(x for x in displayString(string1, string2)))