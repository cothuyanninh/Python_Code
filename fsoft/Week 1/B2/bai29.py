import string
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
#xu li email
while :
	email = input("Email: ")
	if ("@" in email):
		break
	print("Again Email: ")

while :
	password = input("Password: ")
	flag = 0
	for i in lowercase:
		if i in password:
			flag += 1
	for i in uppercase:
		if i in password:
			flag = 1
	for i in digits:
		if i in password:
			flag = 1

	if flag == 0:
