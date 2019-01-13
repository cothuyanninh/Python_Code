import pyperclip , re

phoneRegex = re.compile(r'''(
	\d\d\d\d\d\d\d\d\d\d
	)''', re.VERBOSE)

emailRegex = re.compile('''(
	[a-zA-z0-9._%+-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z]{2,4})
	)''', re.VERBOSE)

text = str(pyperclip.paste())
matches =[]

for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' +groups[8]
	matches.append(phoneNum)

for groups in emailRegex.findall(text):
	matches.append(groups[0])

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
 	print('No phone numbers or email addresses found.')