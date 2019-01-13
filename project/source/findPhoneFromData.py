import re


def regexNumberPhone(lines):
	phoneNumRegex10number = re.compile(r'\s\d\d\d\d\d\d\d\d\d\d\s')
	phoneNumRegex11number = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d\s')
	phoneNumRegex10number1 = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
	mo1 = phoneNumRegex10number.findall(lines)
	mo2 = phoneNumRegex11number.findall(lines)
	mo3 = phoneNumRegex10number1.findall(lines)
	if len(mo1) != 0 :
		return mo1[0].split('\n')[0]
	if len(mo2) != 0 :
		return mo2[0].split('\n')[0]
	if len(mo3) != 0 :
		return mo3[0].split('\n')[0]
	if len(mo1) == 0 and len(mo2) == 0 and len(mo3) == 0:
		return None



def findNumberPhone(data):
	result = []
	data = data.split('\n')
	for i in range(len(data)):
		if regexNumberPhone(data[i]) != None:
			result.append(regexNumberPhone(data[i]))
	if len(result) == 0 :
		return 'Nothing Phone'
	return result[-1]
	
