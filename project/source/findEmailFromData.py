import re
from getDataFromWord import get_docx_text

def regexEmail(lines):
	matches =[]
	emailRegex = re.compile('''(
	[a-zA-z0-9._%+-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
	)''', re.VERBOSE)

	for groups in emailRegex.findall(lines):
		matches.append(groups[0])
	return matches[0]


def findEmail(data):
	result = []
	data = data.split('\n')
	for i in range(len(data)):
		if '@' in data[i]:
			result.append(regexEmail(data[i]))
	if len(result) == 0 :
		return 'Nothing Email'
	if max(result).startswith('Email'):
		return max(result).split('Email')[1]
	return max(result)
