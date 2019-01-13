import re
regex = re.compile(r'\w+')
minh = regex.findall('Tran Cong Minh la 1 nguoi \n \n \t .n  dep trai 1 nhat the gioi nay huihihihii')
for i in range(len(minh)):
	if minh[i].istitle() == True:
		print(minh[i])
