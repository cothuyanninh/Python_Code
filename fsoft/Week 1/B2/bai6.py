while(True):
	number = int(input("Enter a number: "))
	if (number == 0):
		break
	flag = 0
	for i in str(number):
		if int(i) %2 == 1:
			flag = 1
	if flag == 1:
		print("False")
	else:
		print("True")